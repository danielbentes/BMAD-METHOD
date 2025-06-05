# Memory Command Examples

## Good Examples ✅

### /remember Command Examples

#### Example 1: Recording a Technical Decision
```
User: /remember Decided to use PostgreSQL over MongoDB for user data because we need ACID compliance and complex relational queries. Team has more PostgreSQL experience.

Assistant: 💾 Memory Saved

**Category**: Decision (auto-detected)
**Tags**: database, postgresql, architecture, team-skills
**Context**: E-Commerce API project - Architecture phase
**Linked to**: Architect persona, Database Design task

**Memory ID**: decision-2024-01-db-choice
**Confidence**: High (clear rationale provided)

This decision has been linked to similar past decisions for pattern analysis.
```

#### Example 2: Capturing a Successful Pattern
```
User: /remember Starting with API contract design before implementation reduced rework by 70% in the last sprint. Team alignment was much better.

Assistant: 🎯 Pattern Captured

**Category**: Pattern (auto-detected)
**Pattern Type**: Workflow Pattern
**Success Metric**: 70% rework reduction
**Tags**: api-design, workflow, team-alignment

**Pattern Analysis**:
- This is the 3rd occurrence of "API-first" pattern
- Success rate: 100% (3/3 applications)
- Confidence level upgraded: 65% → 78%

Would you like to see similar patterns that might complement this approach?
```

#### Example 3: Learning from Mistakes
```
User: /remember Skipping integration tests caused 5 production bugs. Spent 2 days fixing issues that 2 hours of tests would have caught.

Assistant: 🔴 Mistake Recorded & Analyzed

**Category**: Mistake (auto-detected)
**Impact**: High (production bugs)
**Time Lost**: 2 days vs 2 hours (24x multiplier)
**Tags**: testing, quality, technical-debt

**Anti-Pattern Registered**: "Test Skip Under Pressure"
- This anti-pattern has now occurred 2 times
- Average time penalty: 15x original estimate
- Preventive measure added to quality gates

**Proactive Suggestion**: Would you like me to add integration tests to your current task checklist?
```

### /recall Command Examples

#### Example 1: Natural Language Search
```
User: /recall authentication decisions

Assistant: 🔍 Found 4 relevant memories:

1. **JWT vs Session Auth** (2 weeks ago)
   - Decision: JWT with refresh tokens
   - Reason: Stateless, microservice-friendly
   - Outcome: ✅ Working well, 0 auth issues
   - Relevance: 95%

2. **OAuth Provider Selection** (1 month ago)
   - Decision: Auth0 over custom implementation
   - Reason: Faster time to market, compliance built-in
   - Outcome: ✅ Saved 3 weeks of development
   - Relevance: 87%

3. **Password Policy Pattern** (3 months ago)
   - Pattern: Progressive password requirements
   - Success Rate: 80% user compliance
   - Applied in: 3 projects
   - Relevance: 72%

4. **2FA Implementation Mistake** (6 months ago)
   - Issue: SMS-based 2FA security vulnerabilities
   - Learning: Use app-based TOTP instead
   - Prevention: Added to security checklist
   - Relevance: 68%

💡 Insight: Your authentication decisions tend to favor proven solutions over custom builds (3/4 times).
```

#### Example 2: Context-Aware Recall
```
User: /recall performance optimizations for React

Assistant: 🔍 Found 5 relevant memories for React performance:

1. **React.memo Success Pattern** (1 week ago)
   - Context: Product listing with 1000+ items
   - Solution: Memoized list items, virtual scrolling
   - Result: 60% render time reduction
   - Code Pattern: Available in memory
   - Relevance: 92%

2. **useState Optimization** (2 weeks ago)
   - Issue: Excessive re-renders from state updates
   - Solution: Consolidated state, useReducer for complex state
   - Result: 40% fewer renders
   - Relevance: 88%

3. **Bundle Size Mistake** (1 month ago)
   - Issue: Importing entire lodash library
   - Fix: Tree-shaking with specific imports
   - Saved: 200KB bundle size
   - Learning: Always check bundle analyzer
   - Relevance: 76%

📊 Performance Trend: Your React optimizations show consistent 40-60% improvements when applied.

Would you like to see the specific code patterns for any of these?
```

### /patterns Command Examples

#### Example 1: View All Patterns
```
User: /patterns

Assistant: 🎯 Recognized Patterns in Your Workflow

## High Confidence Patterns (>80%)

### 1. 🥇 API-First Design (Confidence: 89%)
- **Type**: Workflow Pattern
- **Success Rate**: 11/12 (92%)
- **Avg Time Saved**: 2.5 days per feature
- **Best For**: Multi-client applications
- **Key Success Factor**: Complete OpenAPI spec before coding

### 2. 🥈 Incremental Migration (Confidence: 85%)
- **Type**: Technical Pattern  
- **Success Rate**: 7/8 (88%)
- **Risk Reduction**: 75% fewer breaking changes
- **Best For**: Legacy system updates
- **Key Success Factor**: Feature flag everything

## Medium Confidence Patterns (60-80%)

### 3. 🥉 Friday Deployment Freeze (Confidence: 72%)
- **Type**: Process Pattern
- **Success Rate**: 15/22 (68%)
- **Incident Reduction**: 60% fewer weekend issues
- **Trade-off**: Slower feature delivery
- **Context**: Works best with small teams

## Emerging Patterns (<60%)

### 4. 🌱 Pair Programming for Complex Features (Confidence: 45%)
- **Occurrences**: 3 (need 2 more for confidence)
- **Early Results**: Fewer bugs but 40% slower
- **Tracking**: Knowledge transfer quality

💡 Recommendation: Your "API-First Design" pattern has proven highly effective. Consider applying it to your current authentication feature.
```

#### Example 2: Filtered Pattern View
```
User: /patterns --type=technical --success-rate=high

Assistant: 🎯 High-Success Technical Patterns

### 1. ✨ Dependency Injection Pattern (Confidence: 91%)
- **Success Rate**: 18/19 (95%)
- **Benefits**:
  - 80% easier testing
  - 65% fewer coupling issues
  - 90% better maintainability scores
- **Implementation Guide**:
  ```typescript
  // Pattern memorized from your implementations
  interface Dependencies {
    database: Database
    cache: Cache
    logger: Logger
  }
  
  class Service {
    constructor(private deps: Dependencies) {}
  }
  ```

### 2. 🔄 Circuit Breaker for External APIs (Confidence: 88%)
- **Success Rate**: 14/16 (88%)
- **Prevented Outages**: 12
- **Avg Response Time Improvement**: 3x during failures
- **Your Implementation Pattern**:
  - Threshold: 5 failures in 60 seconds
  - Timeout: 30 seconds
  - Half-open retry: After 30 seconds

📈 These patterns have saved an estimated 156 hours of debugging time across your projects.
```

### /insights Command Examples

#### Example 1: Context-Aware Insights
```
User: /insights

Assistant: 💡 Proactive Insights for Your Current Work

## 🚨 Critical Insight
**Missing Test Coverage Pattern Detected**
You're at the same project stage where test skipping occurred in 3 previous projects.
- **Risk**: 80% chance of production bugs without tests
- **Action**: Allocate 2 hours today for core test suite
- **ROI**: Prevent ~16 hours of bug fixes

## ⚡ Quick Win Available
**Caching Opportunity Identified**
Your user profile endpoint matches a pattern that benefited from Redis caching.
- **Expected Improvement**: 65% response time reduction
- **Implementation Time**: 1.5 hours
- **Similar Success**: Applied 4 times with avg 70% improvement

## 📦 Strategic Recommendation  
**Consider Microservice Split**
Based on your codebase growth pattern:
- Auth service has 87% independence score
- Similar projects split at this size with 90% success
- **Timing**: Do before user base 10x growth
- **Effort**: 1 sprint with your team size

## 🔮 Predictions Based on Patterns
1. **Next Bottleneck**: Database connections (2-3 weeks)
2. **Team Request**: Frontend developer for UI work (1 week)  
3. **Stakeholder Concern**: Performance metrics (next review)

Want details on any of these insights?
```

#### Example 2: Focused Insights
```
User: /insights --focus=performance

Assistant: 🎯 Performance-Focused Insights

## 📦 Database Performance
**N+1 Query Pattern Risk: HIGH**
- Detected in: User listing endpoint
- Similar issue caused 3s+ load times in Project Alpha
- **Fix**: Eager loading with `.include()`
- **Effort**: 30 minutes
- **Impact**: 80% query reduction

## ⚡ Caching Opportunities
1. **Static Content** (Immediate)
   - Homepage data changes once/day
   - Cache for 1 hour = 95% hit rate
   - Implementation: 20 minutes

2. **User Preferences** (Quick Win)
   - Read 100x more than written
   - Redis cache = 200ms → 5ms
   - Implementation: 1 hour

## 📈 Performance Trajectory
Based on growth patterns from 6 similar projects:
- Current: 150ms avg response time ✅
- 1 month: 200ms (still acceptable) ⚠️
- 3 months: 450ms (user complaints) 🔴
- **Prevention**: Implement caching layer this sprint

## 🎯 Proven Optimization Sequence
From your successful patterns:
1. Database query optimization (Week 1)
2. API response caching (Week 2)  
3. Frontend bundle optimization (Week 3)
4. CDN implementation (Week 4)

This sequence worked in 4/4 previous optimizations.
```

### /learn Command Examples

#### Example 1: Capturing Positive Outcome
```
User: /learn The API-first approach worked perfectly. Client team could start integration while we built the backend. Zero integration issues at merge.

Assistant: 🎆 Learning Captured Successfully

**Outcome Analysis**:
- Pattern: "API-First Design" 
- Result: SUCCESS (Zero integration issues)
- Time Saved: Parallel development enabled
- Team Satisfaction: High

**Pattern Updates Applied**:
- Confidence: 89% → 92% ✨
- Success Rate: 11/12 → 12/13 (92%)
- New Success Factor Added: "Enables parallel development"
- Context Refinement: "Especially effective with separate teams"

**New Insight Generated**:
"API-first design enables true parallel development between frontend and backend teams"

**Recommendation**: Document the OpenAPI spec you used as a template for future projects?
```

#### Example 2: Learning from Failure
```
User: /learn The microservice split failed. Too early, team wasn't ready, added complexity without benefits. Rolled back after 2 weeks.

Assistant: 🔴 Critical Learning Captured

**Failure Analysis**:
- Pattern: "Early Microservice Split"
- Result: FAILURE (Rolled back)
- Root Causes Identified:
  1. Team size insufficient (3 devs for 4 services)
  2. Traffic didn't justify complexity
  3. Missing DevOps infrastructure

**System Updates**:
1. **Pattern Confidence Adjusted**: 72% → 51% ⚠️
2. **Context Boundaries Refined**:
   - Minimum team size: 5 → 8 developers
   - Minimum traffic: 1K → 10K req/sec
   - Required: Mature CI/CD pipeline

3. **New Anti-Pattern Registered**: 
   "Premature Microservice Split"
   - Warning signs: Team strain, no clear boundaries
   - Prevention: Modular monolith first

4. **Updated Recommendations**:
   - Microservice suggestion threshold raised
   - New prerequisite check: DevOps maturity

**Recovery Insight**: Your quick rollback decision prevented larger issues. This decisive action is now a positive pattern.

Would you like strategies for achieving microservice benefits without the split?
```

## Bad Examples ❌

### Example 1: Vague Memory
**Wrong**:
```
User: /remember Some stuff about databases didn't work well

Assistant: Memory saved.
```

**Why it's wrong**: 
- No specific details captured
- Can't extract patterns or learnings
- No categorization possible
- Won't help in future decisions

**Better**:
```
User: /remember MongoDB performance degraded at 1M documents due to missing indexes on frequently queried fields. Added compound index on (userId, createdAt) - query time went from 2s to 50ms.
```

### Example 2: No Context in Recall
**Wrong**:
```
User: /recall stuff

Assistant: No memories found matching "stuff".
```

**Why it's wrong**:
- Query too vague
- No attempt to understand intent
- No helpful suggestions

**Better**:
```
User: /recall authentication
[Shows relevant auth-related memories with context]
```

### Example 3: Overwhelming Pattern Display
**Wrong**:
```
User: /patterns

Assistant: [Dumps 50 patterns in a huge wall of text with every detail]
```

**Why it's wrong**:
- Information overload
- No prioritization
- Not actionable
- Poor progressive disclosure

### Example 4: Generic Insights
**Wrong**:
```
User: /insights

Assistant: You should write tests and document your code. Performance is important. Consider security.
```

**Why it's wrong**:
- Not specific to context
- No evidence from memories
- Generic advice, not insights
- Not actionable

### Example 5: No Learning Analysis
**Wrong**:
```
User: /learn The feature is done

Assistant: OK, noted.
```

**Why it's wrong**:
- No outcome analysis
- No pattern updates
- No extraction of learnings
- Missed opportunity to improve system

## Progressive Disclosure Examples

### Starting Concise
```
User: /patterns

Assistant: 🎯 Top 3 Patterns:
1. API-First Design (89% confidence) - Saves 2.5 days/feature
2. Incremental Migration (85%) - 75% fewer breaking changes  
3. Test-Driven Development (78%) - 60% fewer bugs

Type "show more" or select a pattern number for details.
```

### Expanding on Request
```
User: 1

Assistant: [Detailed breakdown of API-First Design pattern with examples, success factors, and implementation guide]
```

### Full Detail When Needed
```
User: show all patterns with examples

Assistant: [Comprehensive pattern library with all details, examples, and cross-references]
```