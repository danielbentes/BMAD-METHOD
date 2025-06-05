# Brownfield Analysis Task

## Purpose
Perform comprehensive analysis of existing codebases to extract patterns, decisions, conventions, and team preferences for memory initialization. This task provides detailed instructions for LLMs to systematically analyze brownfield projects.

## Behavioral Requirements

**IMPORTANT**: This is an instruction file that guides LLM behavior. The LLM should follow these analysis steps when performing brownfield codebase analysis.

## Analysis Process

### Phase 1: Initial Project Discovery (5-10 minutes)

#### 1.1 Repository Structure Analysis
```
When analyzing repository structure:
1. Identify primary language(s) from file extensions
2. Detect framework indicators (package.json, requirements.txt, Gemfile, etc.)
3. Map folder organization patterns:
   - Feature-based (features/auth, features/payment)
   - Layer-based (controllers/, models/, views/)
   - Domain-driven (bounded contexts)
   - Module-based organization
4. Note naming conventions for directories
5. Identify special purpose directories (tests, docs, config, scripts)
```

#### 1.2 Technology Stack Detection
```
Look for and document:
- Frontend: React, Vue, Angular, Svelte indicators
- Backend: Express, Django, Rails, Spring patterns
- Database: Connection configs, migration files, ORM usage
- Testing: Jest, pytest, RSpec, testing framework configs
- Build tools: Webpack, Vite, Gradle, Maven configurations
- CI/CD: GitHub Actions, Jenkins, CircleCI configs
```

#### 1.3 Documentation Assessment
```
Evaluate documentation maturity:
1. README completeness (setup, usage, architecture)
2. Inline code documentation density
3. API documentation presence
4. Architecture decision records (ADRs)
5. Contributing guidelines
6. Changelog maintenance
```

### Phase 2: Architectural Pattern Recognition (10-15 minutes)

#### 2.1 Design Pattern Detection
```
Identify common patterns:
- Creational: Factory, Builder, Singleton usage
- Structural: Adapter, Facade, Decorator patterns
- Behavioral: Observer, Strategy, Command patterns
- Architectural: MVC, MVP, MVVM, Clean Architecture
- Domain patterns: Repository, Service layer, DTOs
```

#### 2.2 API Design Analysis
```
For REST APIs:
- Resource naming conventions (plural/singular)
- HTTP verb usage patterns
- Response format consistency
- Error handling approaches
- Authentication/authorization patterns

For GraphQL:
- Schema organization
- Resolver patterns
- Type naming conventions
- Query/mutation structure
```

#### 2.3 Data Flow Patterns
```
Trace data flow to identify:
- State management approach (Redux, MobX, Context)
- Event handling patterns
- Data transformation layers
- Caching strategies
- Real-time communication patterns
```

### Phase 3: Code Quality Analysis (10-15 minutes)

#### 3.1 Coding Conventions
```
Extract style patterns:
1. Naming conventions:
   - Variables: camelCase, snake_case, PascalCase
   - Functions: verb patterns (get*, set*, handle*)
   - Classes: noun patterns, suffixes (Controller, Service)
   - Files: kebab-case, PascalCase, snake_case

2. Code organization:
   - Import grouping and ordering
   - Function/method length preferences
   - Class size and responsibility patterns
   - Comment placement and style

3. Error handling:
   - Exception types and hierarchy
   - Error propagation patterns
   - Logging approaches
   - User-facing error messages
```

#### 3.2 Testing Patterns
```
Analyze test coverage and patterns:
- Test file organization (alongside code vs separate)
- Test naming conventions
- Mocking strategies
- Test data management
- Integration vs unit test balance
- E2E test presence and tools
```

#### 3.3 Performance Patterns
```
Identify optimization approaches:
- Caching implementations
- Database query optimization
- Asset optimization strategies
- Lazy loading patterns
- Performance monitoring integration
```

### Phase 4: Team Workflow Analysis (5-10 minutes)

#### 4.1 Git History Patterns
```
Analyze commit history for:
- Commit message conventions
- Branch naming patterns
- PR/MR size preferences
- Merge vs rebase usage
- Release tagging patterns
```

#### 4.2 Development Workflow
```
Infer from configs and history:
- Code review requirements
- CI/CD pipeline stages
- Deployment strategies
- Environment management
- Feature flag usage
```

#### 4.3 Collaboration Patterns
```
Look for indicators of:
- Team size (contributor count)
- Code ownership patterns
- Documentation culture
- Issue tracking integration
- Communication preferences
```

### Phase 5: Technical Debt Assessment (5-10 minutes)

#### 5.1 Code Smell Detection
```
Identify potential issues:
- Duplicated code patterns
- Long methods/functions
- Large classes
- Deep nesting
- TODO/FIXME density
- Deprecated API usage
```

#### 5.2 Dependency Analysis
```
Evaluate dependencies:
- Outdated packages
- Security vulnerabilities
- Unused dependencies
- Version pinning strategies
- Internal vs external dependencies
```

#### 5.3 Scalability Indicators
```
Assess growth readiness:
- Database schema flexibility
- API versioning approach
- Microservice boundaries
- Performance bottlenecks
- Monitoring coverage
```

## Memory Creation Guidelines

### Decision Memory Template
```json
{
  "type": "decision",
  "category": "architecture|technology|process",
  "decision": "{what was decided}",
  "rationale": "{why this choice}",
  "alternatives_considered": ["option1", "option2"],
  "evidence": "{what proves this was the choice}",
  "confidence": 0.8,
  "impact": "high|medium|low",
  "reversibility": "easy|moderate|difficult"
}
```

### Pattern Memory Template
```json
{
  "type": "pattern",
  "category": "coding|architecture|workflow",
  "pattern_name": "{descriptive name}",
  "description": "{what the pattern does}",
  "usage_count": 10,
  "effectiveness": 0.9,
  "context": "{where/when to use}",
  "example": "{code or description}"
}
```

### Issue Memory Template
```json
{
  "type": "issue",
  "category": "technical-debt|bug|performance",
  "issue": "{problem description}",
  "severity": "critical|high|medium|low",
  "solution": "{how it was/could be solved}",
  "prevention": "{how to avoid in future}",
  "cost": "{effort to fix}"
}
```

### Preference Memory Template
```json
{
  "type": "preference",
  "category": "style|workflow|tool",
  "preference": "{what is preferred}",
  "evidence_count": 20,
  "consistency": 0.95,
  "exceptions": ["{when not followed}"],
  "team_alignment": "strong|moderate|mixed"
}
```

## Analysis Quality Checklist

Before completing brownfield analysis, verify:

- [ ] Repository structure fully mapped
- [ ] Technology stack comprehensively identified
- [ ] At least 5 architectural decisions extracted
- [ ] Coding conventions documented with examples
- [ ] Testing approach understood
- [ ] Team workflow patterns identified
- [ ] Technical debt areas noted
- [ ] 10-15 foundational memories created
- [ ] Bootstrap report generated

## Common Pitfalls to Avoid

1. **Surface-level analysis**: Don't just list technologies; understand WHY they were chosen
2. **Assumption-based decisions**: Extract evidence from code, not assumptions
3. **Ignoring negative patterns**: Document what's NOT working as learning opportunities
4. **Missing team context**: Consider team size and dynamics in pattern analysis
5. **Overlooking evolution**: Note how patterns have changed over time

## Output Requirements

Generate memories in the following priority order:
1. **Critical decisions** that shaped the project
2. **Successful patterns** used consistently
3. **Team preferences** that guide development
4. **Known issues** and their solutions
5. **Optimization opportunities** for future work

Each memory should include:
- Clear categorization
- Confidence scoring
- Supporting evidence
- Actionable insights
- Relationship to other memories