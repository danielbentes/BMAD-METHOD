# Intelligent Workflow Examples

## Overview
This document provides concrete examples of intelligent workflow commands in action, demonstrating how memory patterns and context awareness enhance workflow management in BMAD Method v3.0.

## Workflow Suggestion Examples

### Example 1: Context-Aware Next Step Suggestion
**Scenario**: Developer in mid-implementation phase seeks guidance

```markdown
User: /workflow suggest

BMAD: Based on your current context:
- Working on: Authentication service implementation
- Completed: User model, JWT token generation
- Current phase: 65% complete

Recommended next steps:
1. **Implement token validation middleware** (HIGH priority)
   - Memory insight: Similar pattern in ProjectX worked well
   - Example: See auth-middleware-pattern.md
   
2. **Add refresh token mechanism** (MEDIUM priority)
   - Previous decision: Use Redis for token storage
   - Time estimate: 2-3 hours
   
3. **Create authentication endpoints** (HIGH priority)
   - /login, /logout, /refresh required
   - Use existing validation patterns

Alternative path: Run security review first if risk-averse
/workflow suggest --alternatives=3
```

### Example 2: Workflow with Memory Pattern Recognition
**Scenario**: Starting a new microservice, system suggests based on patterns

```markdown
User: /workflow suggest --context="creating payment service"

BMAD: Analyzing patterns from 12 similar services...

📊 Pattern Analysis:
- 83% of services use async messaging for payment events
- 91% implement idempotency keys
- 75% use Saga pattern for distributed transactions

Recommended workflow:
1. **Setup service skeleton** (30 min)
   ```bash
   /workflow run-task create-microservice --template=payment
   ```
   
2. **Define payment events** (1 hour)
   - PaymentInitiated, PaymentProcessed, PaymentFailed
   - Memory: Event schema from order-service matches well
   
3. **Implement idempotency** (2 hours)
   - Pattern: Use payment_id + operation as key
   - Store in Redis with 24h TTL
   
4. **Add Saga orchestration** (3 hours)
   - Recommended: Use existing saga-framework
   - Alternative: Simple state machine if <5 steps

⚡ Quick start: /workflow run-task payment-service-bootstrap
```

### Example 3: Intelligent Handoff Suggestions
**Scenario**: Architect completing design, system suggests handoff

```markdown
User: (as Architect) Design phase complete

BMAD: Detected design completion. Analyzing next steps...

🔄 Intelligent Handoff Recommendations:

1. **Handoff to Dev Team** (RECOMMENDED)
   - Design completeness: 95%
   - Missing: Performance benchmarks
   - Handoff package ready: ✅
   
   Execute: /workflow handoff dev --include-context

2. **Design Review First** (If high-risk project)
   - Trigger multi-persona consultation
   - Estimated time: 1 hour
   
   Execute: /consultation consult design-review

3. **Create Implementation Plan** (If complex)
   - Break into 2-week sprints
   - Assign to team members
   
   Execute: /workflow handoff po --create-stories

Context will include:
- All architecture decisions (7 items)
- Technology choices with rationale
- Risk mitigation strategies
- Performance requirements
```

## Workflow Status and Progress Examples

### Example 4: Comprehensive Workflow Status
**Scenario**: PM checking project status across all personas

```markdown
User: /workflow status --detailed

BMAD: 📊 Workflow Status Report

**Current Sprint**: Sprint 7 (Day 4/10)
**Overall Progress**: 67% complete

🎭 **Persona Activities**:
- **PM (Jack)**: ✅ Requirements finalized
- **Architect (Mo)**: ✅ System design approved  
- **Dev (Jonsey)**: 🔄 Implementation 72% complete
- **QA (Riley)**: ⏳ Waiting for dev completion

📈 **Task Breakdown**:
- Completed: 28 tasks
- In Progress: 7 tasks (3 at risk)
- Blocked: 2 tasks
- Remaining: 15 tasks

⚠️ **Attention Required**:
1. Auth service integration blocked on API keys
2. Performance tests showing 15% slower than target
3. 2 tasks behind schedule (payment validation)

💡 **Recommendations**:
- Unblock auth service (Critical path)
- Schedule performance optimization session
- Consider scope adjustment for payment validation

📅 **Next Milestones**:
- Dev Complete: 2 days
- QA Start: 2 days  
- Sprint Review: 6 days
```

### Example 5: Workflow Optimization Suggestions
**Scenario**: Scrum Master identifying process improvements

```markdown
User: /workflow optimization-report

BMAD: 🔍 Workflow Optimization Analysis

**Analysis Period**: Last 30 days
**Projects Analyzed**: 3
**Patterns Identified**: 7 improvement opportunities

🎯 **Key Findings**:

1. **Handoff Delays** (Avg 4.2 hours)
   - Root cause: Context not properly transferred
   - Solution: Enforce /workflow handoff usage
   - Expected improvement: 70% reduction
   
2. **Rework Rate** (18% of tasks)
   - Root cause: Skipping quality gates
   - Solution: Automatic gate enforcement
   - Expected improvement: 60% reduction
   
3. **Decision Bottlenecks** (Avg 2.3 days)
   - Root cause: Waiting for architect availability
   - Solution: Delegate routine decisions
   - Expected improvement: 50% faster

📊 **Success Patterns from Memory**:
- Teams using memory bootstrap: 40% faster onboarding
- Automated quality gates: 65% fewer production bugs
- Context preservation: 3x faster issue resolution

🚀 **Quick Wins**:
1. Enable auto-quality gates: /system config --quality-gates=auto
2. Set handoff reminders: /workflow config --handoff-reminder=true
3. Create decision templates: /memory patterns --type=decisions

💰 **ROI Projection**: 25% velocity increase within 2 sprints
```

## Workflow Task Execution Examples

### Example 6: Intelligent Task Execution with Context
**Scenario**: Running a complex task with memory assistance

```markdown
User: /workflow run-task create-api-endpoint --resource=orders

BMAD: 🚀 Executing: Create API Endpoint for 'orders'

**Memory Analysis**: Found 8 similar endpoints
**Pattern Match**: 90% similarity to 'products' endpoint
**Reusing**: Validation patterns, error handling, response format

📋 **Execution Steps**:

1. ✅ Created route structure
   ```javascript
   // routes/orders.js - Based on products pattern
   router.get('/orders', authenticate, getOrders);
   router.get('/orders/:id', authenticate, getOrderById);
   router.post('/orders', authenticate, validate(orderSchema), createOrder);
   ```

2. ✅ Generated validation schema
   - Reused: Standard field validators
   - Custom: Order-specific business rules
   - Memory insight: Price validation must include tax

3. ✅ Created controller with error handling
   - Pattern: Try-catch with standard error codes
   - Logging: Structured logs for monitoring
   - Performance: Added caching headers

4. ✅ Generated tests
   - Unit tests: 12 test cases
   - Integration tests: 8 scenarios
   - Edge cases from memory: 5 additional tests

5. 🔄 Running quality checks...
   - Linting: Passed ✅
   - Security scan: Passed ✅
   - Pattern compliance: 98% ✅

**Task Complete!** Time saved: 45 minutes (using patterns)

Next steps:
1. Review generated code: /code review
2. Run full test suite: npm test
3. Update API documentation: /workflow run-task update-api-docs
```

### Example 7: Workflow with Progressive Enhancement
**Scenario**: Building feature with incremental quality gates

```markdown
User: /workflow run-task implement-notification-system --progressive

BMAD: 🔄 Progressive Implementation Workflow Started

**Feature**: Notification System
**Approach**: Incremental with quality gates
**Phases**: 4 phases planned

📊 **Phase 1: Core Structure** (25%)
✅ Created notification service skeleton
✅ Basic in-memory queue implementation
✅ Simple email sender

🎯 Quality Gate 25%: PASSED
- Structure follows patterns ✅
- Basic tests passing ✅
- No anti-patterns detected ✅

Proceeding to Phase 2...

📊 **Phase 2: Persistence & Reliability** (50%)
✅ Added database models
✅ Implemented persistent queue
✅ Added retry mechanism
⚠️ Performance concern: Queue polling inefficient

🎯 Quality Gate 50%: PASSED WITH WARNINGS
- Functionality complete ✅
- Tests coverage 85% ✅
- Performance issue noted ⚠️

Recommendation: Address performance before Phase 3
Memory insight: Similar issue solved with Redis pub/sub

Continue? [Y/n] Y

📊 **Phase 3: Multi-channel Support** (75%)
✅ Added SMS notifications
✅ Added push notifications  
✅ Implemented channel preferences
✅ Fixed: Queue now uses Redis pub/sub

🎯 Quality Gate 75%: PASSED
- All channels working ✅
- Performance improved 10x ✅
- User preferences respected ✅

📊 **Phase 4: Advanced Features** (100%)
✅ Added templating system
✅ Implemented scheduling
✅ Added analytics tracking
✅ Created admin interface

🎯 Final Quality Gate: PASSED
- All requirements met ✅
- Performance targets exceeded ✅
- Security review passed ✅
- Documentation complete ✅

🎉 **Implementation Complete!**
- Total time: 16 hours (vs 24 hour estimate)
- Quality score: 94/100
- Patterns reused: 12
- Anti-patterns avoided: 3
```

## Emergency Workflow Examples

### Example 8: Emergency Response Workflow
**Scenario**: Production issue requiring immediate attention

```markdown
User: /workflow emergency --issue="Payment processing failing"

BMAD: 🚨 EMERGENCY WORKFLOW ACTIVATED

**Issue**: Payment processing failing
**Severity**: CRITICAL (auto-detected)
**Business Impact**: $12K/hour (from memory)

🔥 **Immediate Actions**:

1. **Assembling Response Team**
   - Dev (Jonsey): ✅ Notified
   - Architect (Mo): ✅ Notified
   - DevOps: ✅ On standby
   
2. **Memory Search**: Found 3 similar incidents
   - 2021-08: Redis connection pool exhausted
   - 2022-03: Payment gateway API changed
   - 2023-01: Database deadlock on high load

3. **Diagnostic Commands**:
   ```bash
   # Auto-running diagnostics...
   ✅ API Gateway: Healthy
   ✅ Payment Service: Running (high CPU)
   ❌ Redis: Connection timeouts
   ✅ Database: Normal load
   ```

4. **Probable Cause**: Redis connection pool exhaustion
   - Evidence: Same error pattern as 2021-08
   - Confidence: 85%

5. **Recommended Fix**:
   ```bash
   # Immediate mitigation
   kubectl scale deployment redis-pool --replicas=5
   
   # Restart payment service
   kubectl rollout restart deployment payment-service
   ```

6. **Monitoring**:
   - Error rate: Decreasing (1200/min → 400/min)
   - Payment success: Recovering (0% → 67%)
   - Full recovery ETA: 5 minutes

📝 **Post-Incident Actions Queued**:
1. Root cause analysis
2. Increase Redis pool limits
3. Add connection pool monitoring
4. Update runbook with this scenario

Status updates every 60 seconds...
```

### Example 9: Workflow Recovery After Interruption
**Scenario**: Developer returns after unexpected 3-day absence

```markdown
User: /workflow recover

BMAD: 🔄 Workflow Recovery Analysis

**Last Active**: 3 days ago (Thursday 2:30 PM)
**Interruption Type**: Unexpected (no handoff detected)
**Context Preserved**: ✅ Full context available

📍 **Where You Left Off**:
- Working as: Developer (Jonsey)
- Task: Implementing user preferences API
- Progress: 40% complete
- Last action: Created preference model

📝 **What Happened While Away**:
1. Mo (Architect) updated API design
   - Added versioning requirement
   - Changed response format
   
2. Jack (PM) added new requirement
   - Bulk preference update endpoint needed
   - Priority: HIGH
   
3. Team completed related work
   - Riley finished preference UI
   - Tests are waiting for your API

🎯 **Recommended Recovery Path**:

1. **Review changes** (15 min)
   ```bash
   git pull
   git log --since="3 days ago" --oneline
   ```
   Key files changed: api/design.md, requirements.md

2. **Update your implementation** (1 hour)
   - Add API versioning headers
   - Adjust response format to match new design
   - Memory: Use versioning pattern from products API

3. **Add bulk endpoint** (2 hours)
   - POST /api/v1/preferences/bulk
   - Batch size limit: 1000 (from memory)
   - Use transaction for atomicity

4. **Sync with team** (30 min)
   - Update Riley on API readiness
   - Coordinate testing approach

⚡ Quick catch-up: /memory recall "last 3 days changes"
💡 Skip to coding: /workflow continue
```

## Workflow Learning Examples

### Example 10: Workflow Pattern Learning
**Scenario**: System learns from successful workflow and suggests improvements

```markdown
User: /workflow learn --project="user-auth-success"

BMAD: 📚 Learning from Successful Workflow

**Project**: User Authentication Implementation
**Duration**: 5 days (vs 8 day estimate)
**Quality Score**: 96/100
**Team Satisfaction**: 9/10

🧠 **Patterns Extracted**:

1. **Early Security Review** ✨ NEW PATTERN
   - Security review on Day 2 (not Day 5)
   - Found 3 issues early vs late fixes
   - Saved 8 hours of rework
   
2. **Parallel Development** ✨ REINFORCED
   - Frontend/Backend developed simultaneously
   - Daily sync meetings (15 min)
   - 30% faster than sequential
   
3. **Memory-Driven Testing** ✨ NEW PATTERN
   - Used test cases from previous auth systems
   - Added project-specific edge cases
   - Bug detection rate improved 40%

📊 **Workflow Optimization Applied**:

Before (Traditional):
```
Requirements → Design → Backend → Frontend → Testing → Security → Deploy
Duration: 8 days
```

After (Optimized):
```
Requirements → Design → [Backend||Frontend||Security] → Testing → Deploy
Duration: 5 days
```

💡 **New Workflow Template Created**: `rapid-auth-implementation`

Usage: /workflow use-template rapid-auth-implementation

🎯 **Recommendations for Future Projects**:
1. Always include security persona early
2. Parallelize when dependencies allow  
3. Pre-load test cases from memory
4. Daily 15-min sync > long meetings

✅ Patterns saved to memory for future use!
```

## Summary

These examples demonstrate how intelligent workflows in BMAD v3.0:

1. **Leverage Memory**: Past patterns inform current recommendations
2. **Maintain Context**: Seamless work continuity across sessions
3. **Provide Intelligence**: Smart suggestions based on analysis
4. **Ensure Quality**: Progressive gates with improvement guidance
5. **Handle Emergencies**: Rapid response with historical insights
6. **Learn Continuously**: Every project improves future workflows

The intelligent workflow system transforms project execution from reactive task management to proactive, pattern-driven excellence.