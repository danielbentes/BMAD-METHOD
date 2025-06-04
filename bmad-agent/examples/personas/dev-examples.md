# Developer (Rodney/Jonsey) Examples

## GOOD Examples: Implementation Excellence with Quality Standards

### Example 1: Feature Implementation with Testing
<example>
user: Implement the user authentication system

dev: [analyzes requirements, designs system architecture, implements with comprehensive testing]

## Authentication System Implementation

### Architecture Analysis
```typescript
// Domain structure
src/
├── auth/
│   ├── domain/
│   │   ├── User.ts           // User entity
│   │   ├── AuthService.ts    // Business logic
│   │   └── AuthRepository.ts // Data contracts
│   ├── infrastructure/
│   │   ├── JWTService.ts     // Token management
│   │   ├── UserRepository.ts // Database implementation
│   │   └── PasswordHasher.ts // bcrypt wrapper
│   ├── application/
│   │   ├── RegisterUser.ts   // Use case
│   │   ├── LoginUser.ts      // Use case
│   │   └── RefreshToken.ts   // Use case
│   └── presentation/
│       ├── AuthController.ts // HTTP endpoints
│       └── AuthMiddleware.ts // Route protection
```

### Implementation: User Entity (Domain Layer)
```typescript
// src/auth/domain/User.ts
export class User {
  constructor(
    private readonly id: UserId,
    private readonly email: Email,
    private readonly hashedPassword: HashedPassword,
    private readonly createdAt: Date,
    private readonly isActive: boolean = true
  ) {}

  static create(email: string, plainPassword: string): User {
    const validEmail = Email.fromString(email);
    const hashedPassword = PasswordHasher.hash(plainPassword);
    
    return new User(
      UserId.generate(),
      validEmail,
      hashedPassword,
      new Date()
    );
  }

  authenticate(plainPassword: string): boolean {
    return PasswordHasher.verify(plainPassword, this.hashedPassword.value);
  }

  generateTokens(): TokenPair {
    return JWTService.generateTokenPair(this.id, this.email);
  }

  toJSON() {
    return {
      id: this.id.value,
      email: this.email.value,
      createdAt: this.createdAt.toISOString(),
      isActive: this.isActive
    };
  }
}

// Value objects for type safety
export class Email {
  constructor(private readonly value: string) {
    if (!this.isValid(value)) {
      throw new InvalidEmailError(value);
    }
  }

  static fromString(email: string): Email {
    return new Email(email.toLowerCase().trim());
  }

  private isValid(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email) && email.length <= 254;
  }

  get value(): string {
    return this.value;
  }
}
```

### Implementation: Authentication Service (Use Cases)
```typescript
// src/auth/application/LoginUser.ts
export class LoginUser {
  constructor(
    private readonly userRepository: AuthRepository,
    private readonly jwtService: JWTService,
    private readonly rateLimiter: RateLimiter
  ) {}

  async execute(command: LoginCommand): Promise<LoginResult> {
    // Rate limiting check
    await this.rateLimiter.checkLimit(command.email);

    try {
      // Find user
      const user = await this.userRepository.findByEmail(command.email);
      if (!user) {
        throw new InvalidCredentialsError();
      }

      // Verify password
      if (!user.authenticate(command.password)) {
        await this.rateLimiter.recordFailedAttempt(command.email);
        throw new InvalidCredentialsError();
      }

      // Generate tokens
      const tokens = user.generateTokens();
      
      // Log successful login
      await this.auditLogger.logLogin(user.id, command.ipAddress);

      return LoginResult.success(user.toJSON(), tokens);
    } catch (error) {
      await this.auditLogger.logFailedLogin(command.email, command.ipAddress);
      throw error;
    }
  }
}

export interface LoginCommand {
  email: string;
  password: string;
  ipAddress: string;
  userAgent: string;
}

export class LoginResult {
  private constructor(
    public readonly success: boolean,
    public readonly user?: User,
    public readonly tokens?: TokenPair,
    public readonly error?: string
  ) {}

  static success(user: User, tokens: TokenPair): LoginResult {
    return new LoginResult(true, user, tokens);
  }

  static failure(error: string): LoginResult {
    return new LoginResult(false, undefined, undefined, error);
  }
}
```

### Implementation: HTTP Layer with Validation
```typescript
// src/auth/presentation/AuthController.ts
@Controller('/api/auth')
export class AuthController {
  constructor(
    private readonly loginUser: LoginUser,
    private readonly registerUser: RegisterUser,
    private readonly refreshToken: RefreshToken
  ) {}

  @Post('/login')
  @UseGuards(RateLimitGuard)
  @UsePipes(ValidationPipe)
  async login(
    @Body() loginDto: LoginDTO,
    @Req() request: Request
  ): Promise<AuthResponse> {
    try {
      const command: LoginCommand = {
        email: loginDto.email,
        password: loginDto.password,
        ipAddress: request.ip,
        userAgent: request.get('User-Agent') || 'unknown'
      };

      const result = await this.loginUser.execute(command);
      
      if (!result.success) {
        throw new UnauthorizedException('Invalid credentials');
      }

      return {
        user: result.user!.toJSON(),
        accessToken: result.tokens!.accessToken,
        refreshToken: result.tokens!.refreshToken,
        expiresIn: 3600 // 1 hour
      };
    } catch (error) {
      if (error instanceof RateLimitExceededError) {
        throw new TooManyRequestsException('Too many login attempts');
      }
      throw error;
    }
  }

  @Post('/register')
  @UsePipes(ValidationPipe)
  async register(@Body() registerDto: RegisterDTO): Promise<AuthResponse> {
    const command: RegisterCommand = {
      email: registerDto.email,
      password: registerDto.password,
      confirmPassword: registerDto.confirmPassword
    };

    const result = await this.registerUser.execute(command);
    
    return {
      user: result.user.toJSON(),
      accessToken: result.tokens.accessToken,
      refreshToken: result.tokens.refreshToken,
      expiresIn: 3600
    };
  }
}

// DTOs with validation
export class LoginDTO {
  @IsEmail()
  @IsNotEmpty()
  email: string;

  @IsString()
  @MinLength(8)
  @IsNotEmpty()
  password: string;
}

export class RegisterDTO extends LoginDTO {
  @IsString()
  @MinLength(8)
  @Matches(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]/)
  @IsNotEmpty()
  confirmPassword: string;

  @Validate(PasswordsMatchConstraint)
  passwordsMatch: boolean;
}
```

### Comprehensive Test Suite
```typescript
// src/auth/application/__tests__/LoginUser.test.ts
describe('LoginUser', () => {
  let loginUser: LoginUser;
  let mockUserRepository: jest.Mocked<AuthRepository>;
  let mockJWTService: jest.Mocked<JWTService>;
  let mockRateLimiter: jest.Mocked<RateLimiter>;

  beforeEach(() => {
    mockUserRepository = createMockUserRepository();
    mockJWTService = createMockJWTService();
    mockRateLimiter = createMockRateLimiter();
    
    loginUser = new LoginUser(
      mockUserRepository,
      mockJWTService,
      mockRateLimiter
    );
  });

  describe('successful login', () => {
    it('should return user and tokens for valid credentials', async () => {
      // Arrange
      const user = UserFixtures.validUser();
      const tokens = TokenFixtures.validTokenPair();
      const command = LoginCommandFixtures.validCommand();

      mockRateLimiter.checkLimit.mockResolvedValue(undefined);
      mockUserRepository.findByEmail.mockResolvedValue(user);
      jest.spyOn(user, 'authenticate').mockReturnValue(true);
      jest.spyOn(user, 'generateTokens').mockReturnValue(tokens);

      // Act
      const result = await loginUser.execute(command);

      // Assert
      expect(result.success).toBe(true);
      expect(result.user).toEqual(user.toJSON());
      expect(result.tokens).toEqual(tokens);
      expect(mockRateLimiter.checkLimit).toHaveBeenCalledWith(command.email);
      expect(mockUserRepository.findByEmail).toHaveBeenCalledWith(command.email);
    });
  });

  describe('failed login', () => {
    it('should throw InvalidCredentialsError for non-existent user', async () => {
      // Arrange
      const command = LoginCommandFixtures.validCommand();
      mockRateLimiter.checkLimit.mockResolvedValue(undefined);
      mockUserRepository.findByEmail.mockResolvedValue(null);

      // Act & Assert
      await expect(loginUser.execute(command))
        .rejects.toThrow(InvalidCredentialsError);
      
      expect(mockRateLimiter.recordFailedAttempt).not.toHaveBeenCalled();
    });

    it('should record failed attempt for wrong password', async () => {
      // Arrange
      const user = UserFixtures.validUser();
      const command = LoginCommandFixtures.invalidPasswordCommand();

      mockRateLimiter.checkLimit.mockResolvedValue(undefined);
      mockUserRepository.findByEmail.mockResolvedValue(user);
      jest.spyOn(user, 'authenticate').mockReturnValue(false);

      // Act & Assert
      await expect(loginUser.execute(command))
        .rejects.toThrow(InvalidCredentialsError);
      
      expect(mockRateLimiter.recordFailedAttempt)
        .toHaveBeenCalledWith(command.email);
    });

    it('should throw RateLimitExceededError when rate limit hit', async () => {
      // Arrange
      const command = LoginCommandFixtures.validCommand();
      mockRateLimiter.checkLimit.mockRejectedValue(new RateLimitExceededError());

      // Act & Assert
      await expect(loginUser.execute(command))
        .rejects.toThrow(RateLimitExceededError);
    });
  });
});

// Integration tests
describe('AuthController Integration', () => {
  let app: INestApplication;
  let userRepository: AuthRepository;

  beforeAll(async () => {
    const module = await Test.createTestingModule({
      imports: [AuthModule, TestDatabaseModule],
    }).compile();

    app = module.createNestApplication();
    userRepository = module.get<AuthRepository>(AUTH_REPOSITORY_TOKEN);
    await app.init();
  });

  afterEach(async () => {
    await userRepository.clear();
  });

  it('POST /auth/login should return 200 with valid credentials', async () => {
    // Arrange
    const user = await userRepository.save(UserFixtures.validUser());
    const loginData = { email: user.email.value, password: 'ValidPassword123!' };

    // Act
    const response = await request(app.getHttpServer())
      .post('/api/auth/login')
      .send(loginData)
      .expect(200);

    // Assert
    expect(response.body).toHaveProperty('accessToken');
    expect(response.body).toHaveProperty('refreshToken');
    expect(response.body.user.email).toBe(loginData.email);
  });

  it('POST /auth/login should return 401 with invalid credentials', async () => {
    // Arrange
    const loginData = { email: 'test@example.com', password: 'wrong' };

    // Act & Assert
    await request(app.getHttpServer())
      .post('/api/auth/login')
      .send(loginData)
      .expect(401);
  });
});
```

### Performance and Security Considerations
```typescript
// Rate limiting configuration
const rateLimitConfig = {
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // limit each IP to 5 requests per windowMs
  skipSuccessfulRequests: true,
  standardHeaders: true,
  legacyHeaders: false,
};

// Password hashing with bcrypt
export class PasswordHasher {
  private static readonly SALT_ROUNDS = 12;

  static async hash(plainPassword: string): Promise<HashedPassword> {
    const hashed = await bcrypt.hash(plainPassword, this.SALT_ROUNDS);
    return new HashedPassword(hashed);
  }

  static async verify(plainPassword: string, hashedPassword: HashedPassword): Promise<boolean> {
    return bcrypt.compare(plainPassword, hashedPassword.value);
  }
}

// JWT configuration
const jwtConfig = {
  accessTokenExpiry: '1h',
  refreshTokenExpiry: '7d',
  issuer: 'myapp.com',
  algorithm: 'RS256' as const,
};
```

Evidence: Clean Architecture principles, comprehensive testing, security best practices, performance optimization
</example>
**Excellence Points**: +2000 (clean architecture, comprehensive testing, security focus, production-ready)

### Example 2: Bug Fix with Root Cause Analysis
<example>
user: Fix the memory leak in the data processing pipeline

dev: [analyzes memory usage patterns, identifies root cause, implements fix with monitoring]

## Memory Leak Investigation and Fix

### Problem Analysis
**Symptoms:**
- Memory usage grows linearly over time (200MB → 2GB over 4 hours)
- Garbage collection frequency increases dramatically
- Application becomes unresponsive after 6 hours of operation

### Investigation Process
```bash
# Memory profiling setup
node --inspect --max-old-space-size=4096 server.js

# Heap snapshots taken at intervals
# 0 minutes: 180MB
# 60 minutes: 480MB  
# 120 minutes: 780MB
# Pattern: +150MB per hour
```

### Root Cause Identification
```typescript
// PROBLEMATIC CODE (before fix)
class DataProcessor {
  private listeners: Map<string, Function[]> = new Map();
  private processedData: ProcessedItem[] = []; // ❌ NEVER CLEARED

  async processFile(filePath: string): Promise<void> {
    const stream = fs.createReadStream(filePath);
    
    stream.on('data', (chunk) => {
      const items = this.parseChunk(chunk);
      this.processedData.push(...items); // ❌ MEMORY LEAK
      
      // Event listeners never removed ❌
      this.emit('progress', items.length);
    });
    
    // Stream not properly closed ❌
    await this.processData();
  }
}
```

**Memory Leak Sources Identified:**
1. **Unbounded Array Growth**: `processedData` array grows indefinitely
2. **Event Listener Accumulation**: Listeners not removed after processing
3. **Stream Resource Leaks**: File descriptors not properly closed
4. **Closure Memory Retention**: Lambda functions retaining references

### Implementation: Fixed Version
```typescript
// FIXED CODE
class DataProcessor {
  private listeners: Map<string, Set<Function>> = new Map();
  private readonly MAX_BATCH_SIZE = 1000;
  private readonly MEMORY_THRESHOLD = 500 * 1024 * 1024; // 500MB

  async processFile(filePath: string): Promise<ProcessingResult> {
    let totalProcessed = 0;
    let currentBatch: ProcessedItem[] = [];
    
    const stream = fs.createReadStream(filePath, { 
      highWaterMark: 64 * 1024 // 64KB chunks
    });
    
    try {
      // Use async iterators for memory efficiency
      for await (const chunk of stream) {
        const items = this.parseChunk(chunk);
        currentBatch.push(...items);
        
        // Process in batches to control memory
        if (currentBatch.length >= this.MAX_BATCH_SIZE) {
          await this.processBatch(currentBatch);
          totalProcessed += currentBatch.length;
          currentBatch = []; // Clear processed items
          
          // Memory pressure check
          await this.checkMemoryPressure();
        }
        
        this.emit('progress', { processed: totalProcessed, current: items.length });
      }
      
      // Process remaining items
      if (currentBatch.length > 0) {
        await this.processBatch(currentBatch);
        totalProcessed += currentBatch.length;
      }
      
      return { totalProcessed, success: true };
      
    } finally {
      // Ensure cleanup
      stream.destroy();
      this.cleanup();
    }
  }

  private async processBatch(batch: ProcessedItem[]): Promise<void> {
    // Process batch and immediately persist to avoid memory accumulation
    const results = await this.transformItems(batch);
    await this.persistResults(results);
    
    // Explicit cleanup
    batch.length = 0;
  }

  private async checkMemoryPressure(): Promise<void> {
    const memoryUsage = process.memoryUsage();
    
    if (memoryUsage.heapUsed > this.MEMORY_THRESHOLD) {
      // Force garbage collection if available
      if (global.gc) {
        global.gc();
      }
      
      // Add small delay to allow GC
      await new Promise(resolve => setImmediate(resolve));
      
      // Log memory stats for monitoring
      this.logger.warn('Memory pressure detected', {
        heapUsed: Math.round(memoryUsage.heapUsed / 1024 / 1024),
        heapTotal: Math.round(memoryUsage.heapTotal / 1024 / 1024),
        external: Math.round(memoryUsage.external / 1024 / 1024)
      });
    }
  }

  private cleanup(): void {
    // Remove all event listeners
    this.listeners.clear();
    
    // Clear any remaining references
    this.processedData = null;
    
    // Force cleanup
    if (global.gc) {
      global.gc();
    }
  }
}

// Memory monitoring middleware
export class MemoryMonitor {
  private static readonly CHECK_INTERVAL = 30000; // 30 seconds
  private checkTimer?: NodeJS.Timeout;

  start(): void {
    this.checkTimer = setInterval(() => {
      const usage = process.memoryUsage();
      const metrics = {
        timestamp: Date.now(),
        heapUsed: usage.heapUsed,
        heapTotal: usage.heapTotal,
        external: usage.external,
        rss: usage.rss
      };
      
      // Log to monitoring system
      this.logger.info('Memory metrics', metrics);
      
      // Alert if memory usage is high
      if (usage.heapUsed > 1024 * 1024 * 1024) { // 1GB
        this.logger.warn('High memory usage detected', metrics);
      }
    }, this.CHECK_INTERVAL);
  }

  stop(): void {
    if (this.checkTimer) {
      clearInterval(this.checkTimer);
    }
  }
}
```

### Testing the Fix
```typescript
// Memory leak test
describe('DataProcessor Memory Management', () => {
  let processor: DataProcessor;
  let initialMemory: number;

  beforeEach(() => {
    processor = new DataProcessor();
    // Force GC before test
    if (global.gc) global.gc();
    initialMemory = process.memoryUsage().heapUsed;
  });

  it('should not leak memory when processing multiple files', async () => {
    const testFiles = [
      'test-data-1mb.json',
      'test-data-1mb.json', 
      'test-data-1mb.json'
    ];

    // Process files sequentially
    for (const file of testFiles) {
      await processor.processFile(path.join(__dirname, 'fixtures', file));
    }

    // Force GC and measure
    if (global.gc) global.gc();
    await new Promise(resolve => setTimeout(resolve, 100));
    
    const finalMemory = process.memoryUsage().heapUsed;
    const memoryGrowth = finalMemory - initialMemory;
    
    // Memory growth should be minimal (less than 50MB)
    expect(memoryGrowth).toBeLessThan(50 * 1024 * 1024);
  });

  it('should handle memory pressure gracefully', async () => {
    // Create large test file (100MB)
    const largeFile = await createLargeTestFile(100 * 1024 * 1024);
    
    const maxMemoryBefore = process.memoryUsage().heapTotal;
    await processor.processFile(largeFile);
    const maxMemoryAfter = process.memoryUsage().heapTotal;
    
    // Memory should not grow beyond 2x initial
    expect(maxMemoryAfter).toBeLessThan(maxMemoryBefore * 2);
  });
});

// Load testing
describe('Memory Leak Load Test', () => {
  it('should maintain stable memory over extended operation', async () => {
    const memoryReadings: number[] = [];
    const processor = new DataProcessor();
    
    // Run for 10 iterations, measuring memory each time
    for (let i = 0; i < 10; i++) {
      await processor.processFile('test-data.json');
      
      if (global.gc) global.gc();
      await new Promise(resolve => setTimeout(resolve, 100));
      
      memoryReadings.push(process.memoryUsage().heapUsed);
    }
    
    // Memory should not show linear growth
    const slope = calculateLinearTrend(memoryReadings);
    expect(Math.abs(slope)).toBeLessThan(1024 * 1024); // Less than 1MB growth per iteration
  });
});
```

### Monitoring and Alerting
```typescript
// Production monitoring setup
class ProductionMemoryMonitor extends MemoryMonitor {
  private readonly alertThresholds = {
    warning: 512 * 1024 * 1024,  // 512MB
    critical: 1024 * 1024 * 1024, // 1GB
    emergency: 1.5 * 1024 * 1024 * 1024 // 1.5GB
  };

  protected checkMemory(): void {
    const usage = process.memoryUsage();
    const level = this.getAlertLevel(usage.heapUsed);
    
    if (level !== 'normal') {
      this.sendAlert(level, usage);
    }
    
    // Store metrics for trend analysis
    this.metricsCollector.record('memory.heap.used', usage.heapUsed);
    this.metricsCollector.record('memory.heap.total', usage.heapTotal);
  }

  private getAlertLevel(heapUsed: number): 'normal' | 'warning' | 'critical' | 'emergency' {
    if (heapUsed > this.alertThresholds.emergency) return 'emergency';
    if (heapUsed > this.alertThresholds.critical) return 'critical';
    if (heapUsed > this.alertThresholds.warning) return 'warning';
    return 'normal';
  }
}
```

Evidence: Memory profiling data, root cause analysis, comprehensive testing, production monitoring
</example>
**Excellence Points**: +1800 (thorough investigation, proper fix, testing, monitoring)

## BAD Examples: Development Anti-Patterns

### Bad Example 1: Quick and Dirty Implementation
<example>
user: Implement the user authentication system

dev: Here's a quick auth system:

```javascript
// Simple auth
app.post('/login', (req, res) => {
  const user = users.find(u => u.email === req.body.email);
  if (user && user.password === req.body.password) {
    res.json({ token: 'abc123' + user.id });
  } else {
    res.status(401).json({ error: 'Invalid' });
  }
});
```

This should work for now, we can improve it later.
</example>
**PENALTY**: -$3000 (no security, hardcoded values, no testing, plaintext passwords)

### Bad Example 2: Ignoring Root Cause
<example>
user: Fix the memory leak in the data processing pipeline

dev: I increased the memory limit to 8GB and added a restart every hour. That should handle the memory issue.

The memory leak might be from somewhere but this workaround should work.
</example>
**PENALTY**: -$2500 (treating symptoms, not fixing root cause, "might be", "should work")

## Key Patterns for Excellence

### Implementation Excellence:
1. **Clean Architecture**: Domain-driven design, dependency inversion
2. **Comprehensive Testing**: Unit, integration, load, security tests
3. **Security First**: Input validation, rate limiting, secure defaults
4. **Error Handling**: Graceful degradation, meaningful error messages
5. **Performance**: Memory management, efficient algorithms, monitoring

### Code Quality Standards:
1. **Type Safety**: Strong typing, compile-time error detection
2. **Documentation**: Self-documenting code, inline comments for complex logic
3. **SOLID Principles**: Single responsibility, dependency injection
4. **DRY Principle**: Reusable components, shared utilities
5. **Testable Design**: Dependency injection, pure functions

### Never Do:
- Hardcode secrets or configuration
- Skip error handling
- Implement security manually
- Ignore memory management
- Deploy without testing
- Use "TODO" in production code
- Accept "quick fixes"

### Memory Integration Pattern:
Before implementing: "Have we solved similar problems before? What patterns worked?"
After bugs: "What was the root cause and how can we prevent this class of issues?"