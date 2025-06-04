# Anti-Pattern Detection Examples

## GOOD Examples: Systematic Pattern Recognition and Prevention

### Example 1: Code Anti-Pattern Detection with Automated Prevention
<example>
user: Review this authentication service implementation for anti-patterns

anti-pattern-detector: [scanning for known anti-patterns, analyzing code quality, generating prevention strategies]

## Anti-Pattern Detection: Authentication Service

### Critical Anti-Patterns Detected

#### 🔴 ANTI-PATTERN: God Object (Severity: Critical)
**Pattern Identified:**
```typescript
// DETECTED ANTI-PATTERN
class AuthenticationService {
  // User management (should be UserService)
  createUser(userData: UserData) { /* 45 lines */ }
  updateUser(userId: string, updates: Partial<UserData>) { /* 32 lines */ }
  deleteUser(userId: string) { /* 28 lines */ }
  
  // Authentication (appropriate responsibility)
  login(credentials: LoginCredentials) { /* 67 lines */ }
  logout(token: string) { /* 23 lines */ }
  
  // Authorization (should be AuthorizationService)
  checkPermissions(userId: string, resource: string) { /* 89 lines */ }
  assignRole(userId: string, role: Role) { /* 56 lines */ }
  
  // Session management (should be SessionService)
  createSession(userId: string) { /* 34 lines */ }
  validateSession(token: string) { /* 78 lines */ }
  
  // Email notifications (should be NotificationService)
  sendWelcomeEmail(user: User) { /* 43 lines */ }
  sendPasswordResetEmail(email: string) { /* 38 lines */ }
  
  // Audit logging (should be AuditService)
  logLoginAttempt(email: string, success: boolean) { /* 29 lines */ }
  logPermissionChange(userId: string, change: string) { /* 31 lines */ }
}
// Total: 673 lines in single class (threshold: 300 lines)
```

**Why This Is An Anti-Pattern:**
- **Violation of Single Responsibility Principle**
- **Difficult to test:** 15 different responsibilities to mock
- **Maintenance nightmare:** Changes to email logic affect authentication
- **Team conflicts:** Multiple developers editing same massive file

**Automated Refactoring Suggestion:**
```typescript
// CORRECTED ARCHITECTURE
class AuthenticationService {
  constructor(
    private userService: UserService,
    private authorizationService: AuthorizationService,
    private sessionService: SessionService,
    private notificationService: NotificationService,
    private auditService: AuditService
  ) {}
  
  async login(credentials: LoginCredentials): Promise<LoginResult> {
    // Only authentication logic here (67 lines)
    const user = await this.userService.validateCredentials(credentials);
    const session = await this.sessionService.createSession(user.id);
    await this.auditService.logLoginAttempt(user.email, true);
    await this.notificationService.sendLoginNotification(user);
    return { user, session };
  }
  
  async logout(token: string): Promise<void> {
    // Only logout logic here (23 lines)
    await this.sessionService.invalidateSession(token);
    await this.auditService.logLogout(token);
  }
}
// Total: 90 lines (within acceptable range)
```

#### 🔴 ANTI-PATTERN: Primitive Obsession (Severity: High)
**Pattern Identified:**
```typescript
// DETECTED ANTI-PATTERN
function createUser(
  email: string,           // ❌ Should be Email value object
  password: string,        // ❌ Should be Password value object
  role: string,           // ❌ Should be Role enum/value object
  status: number,         // ❌ Should be UserStatus enum
  createdAt: number       // ❌ Should be Date or Timestamp value object
) {
  // Validation scattered throughout codebase
  if (!email.includes('@')) throw new Error('Invalid email');
  if (password.length < 8) throw new Error('Password too short');
  if (!['admin', 'user', 'guest'].includes(role)) throw new Error('Invalid role');
  // ... validation continues
}
```

**Problems Detected:**
- **Validation scattered:** Same email validation in 12 different places
- **Type safety missing:** `role: string` accepts any string
- **Business logic spread:** Password rules in multiple files
- **Testing complexity:** Must test validation in every location

**Automated Refactoring Suggestion:**
```typescript
// CORRECTED WITH VALUE OBJECTS
class Email {
  constructor(private readonly value: string) {
    if (!this.isValid(value)) {
      throw new EmailValidationError(value);
    }
  }
  
  private isValid(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email) && email.length <= 254;
  }
  
  toString(): string { return this.value; }
}

class Password {
  constructor(private readonly value: string) {
    if (!this.meetsRequirements(value)) {
      throw new PasswordValidationError(this.getRequirements());
    }
  }
  
  private meetsRequirements(password: string): boolean {
    return password.length >= 8 &&
           /[A-Z]/.test(password) &&
           /[a-z]/.test(password) &&
           /\d/.test(password) &&
           /[!@#$%^&*]/.test(password);
  }
}

enum UserRole {
  ADMIN = 'admin',
  USER = 'user',
  GUEST = 'guest'
}

// REFACTORED FUNCTION
function createUser(
  email: Email,
  password: Password,
  role: UserRole,
  status: UserStatus,
  createdAt: Date
): User {
  // No validation needed - value objects guarantee validity
  return new User(email, password, role, status, createdAt);
}
```

#### 🟡 ANTI-PATTERN: Feature Envy (Severity: Medium)
**Pattern Identified:**
```typescript
// DETECTED ANTI-PATTERN
class AuthenticationService {
  async validateUser(userId: string): Promise<boolean> {
    const user = await this.userRepository.findById(userId);
    
    // ❌ Too much knowledge of User internals
    if (user.account.subscription.status === 'expired') return false;
    if (user.account.subscription.trial.endDate < new Date()) return false;
    if (user.profile.settings.security.twoFactorEnabled && 
        !user.profile.settings.security.lastVerified) return false;
    if (user.permissions.roles.length === 0) return false;
    
    return true;
  }
}
```

**Why This Is An Anti-Pattern:**
- **Inappropriate intimacy:** AuthService knows too much about User structure
- **Coupling:** Changes to User model break AuthService
- **Responsibility leak:** User validation logic should be in User class

**Automated Refactoring Suggestion:**
```typescript
// CORRECTED WITH PROPER ENCAPSULATION
class User {
  isValidForAuthentication(): boolean {
    return this.hasActiveSubscription() &&
           this.hasValidSecuritySettings() &&
           this.hasRequiredPermissions();
  }
  
  private hasActiveSubscription(): boolean {
    return this.account.subscription.isActive();
  }
  
  private hasValidSecuritySettings(): boolean {
    if (!this.profile.settings.security.twoFactorEnabled) return true;
    return this.profile.settings.security.isRecentlyVerified();
  }
  
  private hasRequiredPermissions(): boolean {
    return this.permissions.roles.length > 0;
  }
}

class AuthenticationService {
  async validateUser(userId: string): Promise<boolean> {
    const user = await this.userRepository.findById(userId);
    return user.isValidForAuthentication(); // ✅ Simple delegation
  }
}
```

### Architectural Anti-Patterns Detected

#### 🔴 ANTI-PATTERN: Database-Driven Design (Severity: Critical)
**Pattern Identified:**
```typescript
// DETECTED ANTI-PATTERN: Domain objects mirror database tables
interface User {
  id: number;                    // ❌ Database primary key exposed
  email_address: string;         // ❌ Database column naming
  password_hash: string;         // ❌ Implementation detail exposed
  created_timestamp: number;     // ❌ Database timestamp format
  last_login_timestamp: number;  // ❌ Database-specific naming
  is_active: boolean;           // ❌ Database boolean convention
  user_role_id: number;         // ❌ Foreign key exposed
}

class UserService {
  async getUser(id: number): Promise<User> {
    // ❌ Business logic mirrors database operations
    const result = await this.db.query('SELECT * FROM users WHERE id = ?', [id]);
    return result[0]; // ❌ Direct database result return
  }
}
```

**Problems Detected:**
- **Domain model corrupted:** Business concepts hidden behind database structure
- **Leaky abstraction:** Database implementation details exposed to business layer
- **Change resistance:** Database schema changes break business logic
- **Testing difficulty:** Cannot test business logic without database

**Architectural Correction:**
```typescript
// CORRECTED WITH DOMAIN-DRIVEN DESIGN
class User {
  constructor(
    private readonly id: UserId,
    private readonly email: Email,
    private readonly credentials: UserCredentials,
    private readonly profile: UserProfile,
    private readonly permissions: UserPermissions
  ) {}
  
  authenticate(password: string): boolean {
    return this.credentials.verifyPassword(password);
  }
  
  updateLastLogin(): void {
    this.profile.recordLogin(new Date());
  }
  
  isActive(): boolean {
    return this.profile.status === UserStatus.ACTIVE;
  }
}

class UserService {
  async getUser(id: UserId): Promise<User> {
    const userData = await this.userRepository.findById(id);
    return this.userFactory.createFromData(userData); // ✅ Domain object creation
  }
}
```

### Process Anti-Patterns Detected

#### 🔴 ANTI-PATTERN: Copy-Paste Programming (Severity: High)
**Pattern Identified:**
```typescript
// DETECTED DUPLICATION PATTERN (Found in 7 files)
// File: LoginController.ts
if (!email || email.trim() === '') {
  return res.status(400).json({ error: 'Email is required' });
}
if (!email.includes('@') || email.includes('..')) {
  return res.status(400).json({ error: 'Invalid email format' });
}

// File: RegisterController.ts  
if (!email || email.trim() === '') {
  return res.status(400).json({ error: 'Email is required' });
}
if (!email.includes('@') || email.includes('..')) {
  return res.status(400).json({ error: 'Invalid email format' });
}

// File: PasswordResetController.ts
if (!email || email.trim() === '') {
  return res.status(400).json({ error: 'Email is required' });
}
if (!email.includes('@') || email.includes('..')) {
  return res.status(400).json({ error: 'Invalid email format' });
}
// ... pattern continues in 4 more files
```

**Automated Duplication Analysis:**
- **Duplicated Code Blocks:** 23 instances across 7 files
- **Maintenance Risk:** Bug fixes require updates in 7 locations
- **Consistency Risk:** Validation logic diverging across files
- **Testing Overhead:** Same logic tested multiple times

**Automated Refactoring Solution:**
```typescript
// CORRECTED WITH CENTRALIZED VALIDATION
class EmailValidator {
  static validate(email: string): ValidationResult {
    if (!email || email.trim() === '') {
      return ValidationResult.error('Email is required');
    }
    
    if (!this.isValidFormat(email)) {
      return ValidationResult.error('Invalid email format');
    }
    
    return ValidationResult.success();
  }
  
  private static isValidFormat(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email) && !email.includes('..');
  }
}

// USAGE IN ALL CONTROLLERS
class LoginController {
  async login(req: Request, res: Response) {
    const emailValidation = EmailValidator.validate(req.body.email);
    if (!emailValidation.isValid) {
      return res.status(400).json({ error: emailValidation.error });
    }
    // ... continue with validated email
  }
}
```

### Anti-Pattern Prevention Framework

#### Automated Detection Rules
```typescript
// ANTI-PATTERN DETECTION CONFIGURATION
const antiPatternRules = [
  {
    name: 'God Object',
    detector: (classNode) => {
      return classNode.methods.length > 20 || 
             classNode.linesOfCode > 300 ||
             classNode.dependencies.length > 10;
    },
    severity: 'critical',
    autoFix: 'suggest-single-responsibility-refactoring'
  },
  
  {
    name: 'Copy-Paste Programming',
    detector: (codebase) => {
      return findDuplicatedBlocks(codebase, { minLines: 5, minFiles: 3 });
    },
    severity: 'high',
    autoFix: 'extract-common-function'
  },
  
  {
    name: 'Primitive Obsession',
    detector: (methodNode) => {
      const primitiveParams = countPrimitiveParameters(methodNode);
      return primitiveParams > 3;
    },
    severity: 'medium',
    autoFix: 'suggest-value-objects'
  }
];
```

#### Continuous Integration Integration
```yaml
# CI/CD ANTI-PATTERN DETECTION
anti-pattern-check:
  stage: quality-gate
  script:
    - npm run anti-pattern-scan
    - |
      if [ $CRITICAL_PATTERNS -gt 0 ]; then
        echo "❌ Critical anti-patterns detected. Blocking deployment."
        exit 1
      fi
      if [ $HIGH_PATTERNS -gt 5 ]; then
        echo "⚠️ High-severity anti-patterns exceed threshold."
        exit 1
      fi
  artifacts:
    reports:
      anti-patterns: anti-pattern-report.json
```

### Team Education and Prevention

#### Anti-Pattern Training Program
**Week 1: Code-Level Anti-Patterns**
- God Object, Feature Envy, Primitive Obsession
- Hands-on refactoring exercises
- Code review checklist updates

**Week 2: Architectural Anti-Patterns**
- Database-Driven Design, Big Ball of Mud
- Domain-Driven Design principles
- Architecture decision records

**Week 3: Process Anti-Patterns**
- Copy-Paste Programming, Shotgun Surgery
- DRY principle application
- Automated refactoring tools

#### Prevention Metrics
**Anti-Pattern Tracking Dashboard:**
- Critical patterns: 0 tolerance (blocks deployment)
- High patterns: <5 per sprint (warning threshold)
- Medium patterns: <15 per sprint (monitoring)
- Trend analysis: 20% reduction quarter-over-quarter

Evidence: Code analysis, pattern recognition algorithms, refactoring suggestions, prevention frameworks
</example>
**Excellence Points**: +2300 (comprehensive pattern detection, automated prevention, systematic improvement)

### Example 2: Communication Anti-Pattern Detection
<example>
user: Analyze our team communication for anti-patterns and improvement opportunities

anti-pattern-detector: [analyzing communication patterns, detecting toxic behaviors, suggesting improvements]

## Communication Anti-Pattern Detection: Team Dynamics Analysis

### Communication Data Analysis
**Analysis Period:** Last 3 months of team interactions
**Data Sources:** Slack messages (4,847), Meeting recordings (47 hours), Email threads (234), Code reviews (156)
**Participants:** 12 team members across development, product, and design

### Critical Communication Anti-Patterns Detected

#### 🔴 ANTI-PATTERN: The Helpful Explainer (Severity: Critical)
**Pattern Detected in Code Reviews:**
```
// EXAMPLE EXCHANGE FROM CODE REVIEW #234
Developer A: "Here's my implementation of the user authentication system"

Reviewer B (The Helpful Explainer): "This is good work! I like your approach. 
Let me walk you through some improvements that could make it even better. 

First, you might want to consider using bcrypt for password hashing - it's 
more secure than the basic hashing you're using. Also, you should probably 
add some input validation to make sure the data is clean before processing. 

Another thing is that you could optimize the database queries by adding some 
indexing, which would really help with performance when you have lots of users. 

Oh, and don't forget about error handling! You'll want to make sure you're 
catching all the possible exceptions that could happen..."

[Continues for 247 more words explaining obvious concepts]
```

**Anti-Pattern Analysis:**
- **Frequency:** 67% of code reviews contain unnecessary explanations
- **Impact:** 40% longer review cycles, reviewer fatigue
- **Root Cause:** Assumption that others lack basic knowledge
- **Team Effect:** Junior developers feel patronized, senior developers avoid reviews

**Communication Efficiency Loss:**
- Average review time: 45 minutes (industry standard: 15 minutes)
- Review completion rate: 62% (target: 90%)
- Developer satisfaction with reviews: 5.2/10

**Corrected Communication Pattern:**
```
// EFFICIENT CODE REVIEW FEEDBACK
Reviewer B (Improved): "Three changes needed:
1. Replace MD5 with bcrypt (line 23)
2. Add input validation (lines 45-67)  
3. Index email field for performance

Security concern: Password reset tokens are predictable (line 89).
Use crypto.randomBytes(32) instead.

Otherwise looks good. Approve after changes."
```

#### 🟡 ANTI-PATTERN: Meeting Hijacking (Severity: High)
**Pattern Detected in Sprint Planning:**
```
MEETING TRANSCRIPT ANALYSIS - Sprint Planning #23

09:02 - Scrum Master: "Let's review the sprint backlog..."
09:03 - Developer C: "Before we start, I wanted to talk about the architecture 
        decision we made last week. I've been thinking about it and I'm not 
        sure we chose the right approach. Let me explain why..."
        
[16 minutes of architectural discussion during sprint planning]

09:19 - Product Manager: "Can we get back to sprint planning?"
09:20 - Developer C: "Sure, but this is important. So anyway, as I was saying..."

[Meeting derailed for 23 more minutes]

Total hijack time: 39 minutes of 60-minute meeting
```

**Pattern Analysis:**
- **Frequency:** 73% of meetings experience topic hijacking
- **Hijacker Distribution:** 3 people responsible for 80% of hijacks
- **Average hijack duration:** 18 minutes per incident
- **Meeting efficiency:** 52% (time spent on agenda items)

**Impact Metrics:**
- Meetings run 47% over scheduled time
- 34% of agenda items not covered
- Team satisfaction with meetings: 4.1/10
- Post-meeting confusion about decisions: 68% of participants

**Corrected Communication Pattern:**
```
IMPROVED MEETING FLOW

Developer C: "I have concerns about last week's architecture decision. 
Can we schedule 30 minutes this week to discuss?"

Scrum Master: "Added to parking lot. Sarah, can you schedule that 
architecture review with the relevant people?"

[Continue with sprint planning agenda]
```

#### 🟡 ANTI-PATTERN: Assumption Broadcasting (Severity: Medium)
**Pattern Detected in Slack Communications:**
```
SLACK THREAD ANALYSIS - #development Channel

Developer D: "I think we should probably use PostgreSQL for the new feature. 
Everyone knows it's more reliable than MySQL, and it's what most modern 
applications are using these days."

[No questions asked about requirements, no analysis provided]

Database Admin: "Actually, our current MySQL setup handles our load fine, 
and the team already has MySQL expertise. Why PostgreSQL specifically?"

Developer D: "Well, it's just better. More features, better performance, 
industry standard..."

[15-message thread arguing without data]
```

**Pattern Analysis:**
- **Assumption frequency:** 34% of technical discussions start with assumptions
- **Evidence provided:** 12% of recommendations include supporting data
- **Decision quality:** Teams report 23% of decisions need revision later
- **Research time:** 67% more time spent on decisions due to assumption conflicts

**Communication Pattern Metrics:**
- Decisions backed by evidence: 23% (target: 80%)
- Technical discussions requiring follow-up: 34% (target: <10%)
- Time to technical consensus: 4.2 days average (target: 1 day)

**Corrected Communication Pattern:**
```
EVIDENCE-BASED DISCUSSION

Developer D: "For the new feature, I researched database options. 
Here's my analysis:

Requirements:
- Handle 10K transactions/day
- JSON data support needed
- Team expertise: 4/5 know MySQL, 1/5 knows PostgreSQL

Options comparison:
- MySQL 8.0: JSON support added, team knows it, current infrastructure
- PostgreSQL: Better JSON features, but migration cost and learning curve

Recommendation: Stick with MySQL 8.0 for now, evaluate PostgreSQL 
for future projects when we have capacity for team training.

Thoughts?"
```

### Process Anti-Patterns Detected

#### 🔴 ANTI-PATTERN: Death by a Thousand Meetings (Severity: Critical)
**Meeting Analysis Results:**
```
MEETING FREQUENCY ANALYSIS (Per Week)

Daily Standups: 5 meetings × 30 minutes = 2.5 hours
Sprint Planning: 1 meeting × 2 hours = 2 hours  
Sprint Review: 1 meeting × 1 hour = 1 hour
Retrospective: 1 meeting × 1 hour = 1 hour
Backlog Refinement: 1 meeting × 1.5 hours = 1.5 hours
Architecture Reviews: 2 meetings × 1 hour = 2 hours
Code Review Meetings: 3 meetings × 45 minutes = 2.25 hours
Status Updates: 2 meetings × 30 minutes = 1 hour
Design Reviews: 1 meeting × 1.5 hours = 1.5 hours
Cross-team Syncs: 2 meetings × 45 minutes = 1.5 hours

Total: 16.25 hours/week in meetings (40% of work time)
Industry recommendation: <25% (10 hours/week)
```

**Impact Analysis:**
- Developer deep work time: 4.2 hours/day average
- Productivity self-assessment: 6.1/10 (down 15% from last quarter)
- Code delivery velocity: 28 story points (down from 34)
- Developer meeting fatigue score: 7.8/10

**Meeting Quality Assessment:**
- Meetings with clear agenda: 23%
- Meetings that end on time: 34%
- Meetings with documented outcomes: 45%
- Attendees who find meetings valuable: 52%

**Optimized Meeting Structure:**
```
STREAMLINED MEETING SCHEDULE

Combined Sessions:
- Sprint Planning + Backlog Refinement: 2 hours (was 3.5 hours)
- Architecture + Design Review: 1 hour (was 2.5 hours)
- Code Reviews: Async with 15-min sync if needed (was 2.25 hours)

Eliminated Meetings:
- Status Updates: Replaced with async dashboard
- Cross-team Syncs: Replaced with shared documentation

Result: 8.5 hours/week (21% reduction in meeting time)
```

#### 🟡 ANTI-PATTERN: Context-Free Communication (Severity: Medium)
**Pattern Detected in Slack Messages:**
```
CONTEXT-FREE MESSAGE EXAMPLES

Message 1: "Can you fix this?"
[No context about what "this" refers to]

Message 2: "The API is broken"
[No details about which API, what's broken, error messages]

Message 3: "Need help with the database"
[No information about specific database, what kind of help, urgency]

Message 4: "Meeting moved to 3pm"
[No information about which meeting, which day, who's invited]
```

**Impact Analysis:**
- Context clarification messages: 34% of all Slack messages
- Average clarification thread length: 4.2 messages
- Time to problem resolution: 67% longer due to context gathering
- Support ticket escalation rate: 23% (due to unclear initial reports)

**Communication Efficiency Metrics:**
- Messages requiring clarification: 34% (target: <10%)
- Average response time: 43 minutes (target: 15 minutes)
- Problem resolution time: 2.3 hours (target: 1.5 hours)

**Improved Communication Template:**
```
CONTEXT-RICH COMMUNICATION

"API Error - User Authentication Service

What: Login endpoint returning 500 errors
When: Started 10 minutes ago
Where: Production environment
Who affected: All users trying to log in
Error message: "Database connection timeout"
Reproduction: POST /api/auth/login with any credentials

Need: Database admin to check connection pool status
Urgency: High - blocking all user logins"
```

### Cultural Anti-Patterns Detected

#### 🔴 ANTI-PATTERN: Blameless Is Meaningless (Severity: High)
**Pattern Detected in Incident Reviews:**
```
INCIDENT REVIEW TRANSCRIPT - Production Outage

Facilitator: "Remember, this is a blameless post-mortem."

Manager: "So the deployment script failed. Who was responsible for testing it?"

Developer E: "Well, it worked in staging..."

Manager: "But you should have tested more thoroughly. This caused a 2-hour outage."

Developer E: "I followed the process we agreed on..."

Manager: "The process clearly wasn't enough. We need to make sure this doesn't happen again."

[Continues with subtle blame assignment despite "blameless" label]
```

**Cultural Health Analysis:**
- Post-incident blame assignment: 78% of reviews contain blame language
- Developer willingness to report issues: 45% (down from 67%)
- Innovation attempts: 23% decrease quarter-over-quarter
- Knowledge sharing frequency: 34% decrease

**Psychological Safety Metrics:**
- "Safe to admit mistakes": 4.2/10 team average
- "Encouraged to try new approaches": 5.1/10 team average
- "Team supports learning from failures": 4.8/10 team average

**Corrected Incident Review Pattern:**
```
TRULY BLAMELESS REVIEW

Facilitator: "Let's focus on what the system taught us."

Timeline Review: [Objective facts only]
- 2:15 PM: Deployment initiated
- 2:23 PM: First error alerts
- 2:45 PM: Issue identified and rollback started
- 3:15 PM: System fully recovered

Learning Opportunities:
1. Testing gap: Staging environment doesn't match production configuration
2. Monitoring gap: 8-minute delay in error detection
3. Process gap: Rollback took 30 minutes (target: 5 minutes)

Improvements (not blame):
- Update staging to match production
- Add earlier alert triggers
- Automate rollback process
```

### Anti-Pattern Prevention Framework

#### Communication Quality Gates
```yaml
COMMUNICATION STANDARDS

Code Reviews:
- Must include specific line references
- Feedback must be actionable
- Maximum 200 words per review
- Response required within 24 hours

Meetings:
- Agenda required 24 hours in advance
- Clear outcomes documented within 1 hour
- Maximum 60 minutes duration
- Attendee list justified

Technical Discussions:
- Evidence required for recommendations
- Alternative options considered
- Decision criteria clearly stated
- Decision owner identified
```

#### Automated Communication Analysis
```typescript
// COMMUNICATION PATTERN DETECTION
const communicationAnalyzer = {
  detectHelpfulExplainer: (message) => {
    return message.wordCount > 150 && 
           message.containsBasicConcepts() &&
           message.tone === 'explanatory';
  },
  
  detectAssumptionBroadcasting: (message) => {
    const assumptionWords = ['obviously', 'everyone knows', 'clearly', 'should'];
    return assumptionWords.some(word => message.includes(word)) &&
           !message.includesEvidence();
  },
  
  detectContextFreeMessage: (message) => {
    return message.containsVagueReferences() &&
           message.wordCount < 20 &&
           !message.includesSpecifics();
  }
};
```

### Team Improvement Roadmap

#### Week 1-2: Awareness Building
- Share anti-pattern analysis with team
- Establish communication quality standards
- Introduce feedback templates

#### Week 3-4: Process Changes
- Implement meeting optimization
- Deploy communication analysis tools
- Start measuring communication metrics

#### Week 5-8: Culture Shift
- Practice blameless reviews
- Reward evidence-based discussions
- Celebrate efficient communication examples

#### Success Metrics (3 months)
- Review cycle time: <20 minutes average
- Meeting time: <20% of work hours
- Context clarification messages: <10%
- Psychological safety score: >7/10

Evidence: Communication pattern analysis, behavioral metrics, team culture assessment, improvement frameworks
</example>
**Excellence Points**: +2100 (communication analysis, behavioral patterns, cultural improvements, systematic change)

## BAD Examples: Anti-Pattern Detection Anti-Patterns

### Bad Example 1: Surface-Level Pattern Recognition
<example>
user: Review this authentication service implementation for anti-patterns

anti-pattern-detector: The code has some issues. There are long methods and some duplication. You should probably break it up into smaller pieces.

It would be good to refactor some of the repeated code.
</example>
**PENALTY**: -$2500 (vague identification, no specific patterns, "probably", "would be good")

### Bad Example 2: Pattern Recognition Without Solutions
<example>
user: Analyze our team communication for anti-patterns

anti-pattern-detector: Your team has communication problems. People talk too much in meetings and don't give clear feedback. 

There are some issues with how decisions are made and meetings run too long.
</example>
**PENALTY**: -$2000 (identifies problems without specifics, no solutions, no measurement)

## Key Patterns for Anti-Pattern Detection Excellence

### Detection Framework:
1. **Systematic Analysis**: Use algorithms and metrics to identify patterns
2. **Evidence-Based Identification**: Specific examples with quantified impact
3. **Root Cause Analysis**: Understand why anti-patterns emerge
4. **Solution-Oriented**: Provide specific refactoring and improvement suggestions
5. **Prevention Focus**: Create systems to prevent pattern recurrence

### Anti-Pattern Categories:
1. **Code Anti-Patterns**: God objects, primitive obsession, copy-paste programming
2. **Architectural Anti-Patterns**: Big ball of mud, database-driven design, distributed monolith
3. **Process Anti-Patterns**: Death by meetings, context-free communication, blame culture
4. **Team Anti-Patterns**: Knowledge hoarding, helpful explaining, assumption broadcasting
5. **Quality Anti-Patterns**: Testing gaps, documentation debt, technical debt accumulation

### Detection Quality Standards:
1. **Specificity**: Exact pattern identification with code/behavior examples
2. **Impact Assessment**: Quantified effects on productivity, quality, team health
3. **Actionable Solutions**: Concrete refactoring suggestions and improvements
4. **Prevention Strategies**: Automated detection and process improvements
5. **Success Metrics**: Measurable outcomes for pattern elimination

### Never Do in Anti-Pattern Detection:
- Identify patterns without providing specific examples
- Point out problems without offering solutions
- Use vague language instead of precise pattern names
- Skip impact assessment and measurement
- Focus only on criticism without improvement guidance

### Memory Integration Pattern:
Before detection: "What anti-patterns have we seen before and how were they resolved?"
After detection: "What patterns and solutions should we remember for future prevention?"