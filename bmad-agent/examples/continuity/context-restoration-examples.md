# Context Restoration Examples

## Good Examples ✅

### Example 1: Quick Resume (< 2 hours)
**Scenario**: Developer returns after a coffee break

```
User: Hi, I'm back

Assistant: 🔄 Welcome back! Continuing from 45 minutes ago...

**Last activity**: Implementing payment webhook handler
**Progress**: 65% complete

Ready to continue? Type /continue or start with your question.
```

### Example 2: Full Context Restoration (Half Day Gap)
**Scenario**: Developer returns after lunch and meetings

```
User: Hello, back to work on the API

Assistant: 🔄 Welcome back!

## Last Context Summary
**When**: 4 hours ago
**Duration**: 3 hours
**Active Persona**: Developer (Jonsey)
**Last Activity**: Payment gateway integration

## What's Changed Since You Left
📝 **New commits** (by others):
- Fix: Resolved CORS issue in API endpoints (@sarah)
- Feature: Added rate limiting to auth endpoints (@john)

💡 **Memory Insights**:
- Webhook security pattern from last project would apply here
- Consider implementing idempotency keys (worked in 3 similar integrations)

## Continue Where You Left Off?
- [x] Resume: Payment webhook handler (65% complete)
- [ ] Review: New rate limiting implementation
- [ ] Test: CORS fix impact on payment endpoints

Type `/continue` to resume or choose a priority above.
```

### Example 3: Extended Gap with Priority Shifts
**Scenario**: Developer returns after 2 days

```
User: /context

Assistant: 🔄 Project Context Restoration

## Time Away: 2 days

## Project Status Overview
**Sprint Progress**: Day 10 of 14
**Overall Progress**: 58% → 71% (+13%)

## Key Developments While Away
1. **Completed by team**:
   - ✅ User authentication module (@mike)
   - ✅ Database migration scripts (@sarah)
   - ✅ CI/CD pipeline setup (@devops)

2. **New Priorities**:
   - 🔴 Payment integration (your work) - now BLOCKING release
   - 🟡 Performance issue in search API - customer reported
   - 🟢 Documentation updates - can wait

3. **Important Decisions**:
   - Team decided to use Redis for session management
   - API versioning strategy changed to header-based
   - Deploy moved to Friday (was Wednesday)

## Recommended Next Steps
Based on priorities and your 65% complete payment work:
1. Complete payment webhook handler (est. 2 hours)
2. Test with new Redis session setup
3. Address any API versioning impacts

Would you like a detailed briefing on any area?
```

### Example 4: Multi-Project Context Switch
**Scenario**: Developer working on multiple projects

```
User: What projects do I have?

Assistant: 📁 Available Projects

### 1. **E-Commerce API** ⚡ (Last Active)
- **Path**: ~/projects/ecommerce-api
- **Last Active**: 2 days ago
- **Status**: Payment integration (65%)
- **Branch**: feature/payment-gateway
- **Quick Switch**: `/project switch ecommerce-api`

### 2. **Analytics Dashboard**
- **Path**: ~/projects/analytics-dash
- **Last Active**: Yesterday at 2:30 PM
- **Status**: Fixing chart memory leak
- **Branch**: bugfix/chart-performance
- **Quick Switch**: `/project switch analytics-dash`

### 3. **Mobile App**
- **Path**: ~/projects/mobile-app
- **Last Active**: 1 week ago
- **Status**: Implementing push notifications
- **Branch**: feature/push-notifications
- **Quick Switch**: `/project switch mobile-app`

💡 Based on your patterns, you typically work on Analytics Dashboard on Thursdays.

Which project would you like to switch to?
```

### Example 5: Smart Continuation with Conflicts
**Scenario**: Returning with uncommitted changes

```
User: Continue where I left off

Assistant: ⚠️ Context Restoration Notice

**Saved context**: Working on payment integration
**Current state**: Uncommitted changes detected

```bash
Modified files:
- src/payments/webhook.js (2 changes)
- tests/payments.test.js (5 changes)
```

## Your Options:
1. **Stash and restore** - Save current changes, restore exact context
2. **Merge contexts** - Keep changes and update context
3. **Review first** - See diff before deciding

What would you prefer? (1/2/3)

User: 2

Assistant: ✅ Contexts merged successfully

**Current State**:
- Payment integration: 65% → 70% (detected progress)
- Webhook handler: Basic implementation added
- Tests: 5 new test cases detected

**Next recommended steps**:
1. Complete webhook signature validation
2. Add error handling for timeout scenarios
3. Run test suite to verify changes

Ready to continue with `/continue` or need more details?
```

## Bad Examples ❌

### Example 1: No Context Awareness
**Wrong**:
```
User: I'm back

Assistant: Hello! How can I help you today?
```

**Why it's wrong**: Doesn't recognize returning user or restore any context

### Example 2: Overwhelming Information
**Wrong**:
```
User: Continue

Assistant: [500 lines of every single change, commit, file modification, memory item, decision, etc.]
```

**Why it's wrong**: Information overload, not progressive disclosure

### Example 3: Technical Jargon
**Wrong**:
```
User: What was I working on?

Assistant: Session ID abc-123-def has context state in /Users/dev/.bmad/state/context-state.md with memory pointers to OpenMemory indices 45-89...
```

**Why it's wrong**: Exposes internal technical details instead of user-friendly summary

## Progressive Disclosure Examples

### Starting Concise
```
User: /context

Assistant: 🔄 E-Commerce API | Payment integration (65%) | Away: 3 hours
💡 Team completed auth module while away
⚡ Type `/continue` to resume or `tell me more` for details
```

### Expanding on Request
```
User: tell me more

Assistant: 
## Detailed Context Update

**Your Work**: Payment webhook handler
- Completed: Basic endpoint structure
- In Progress: Signature validation
- Next: Error handling and retries

**Team Activity**:
- Mike: Finished auth module, all tests passing
- Sarah: Updated database schemas, migration ready
- John: Fixed CORS issues in API gateway

**New Decisions**:
- Redis for sessions (replaces in-memory)
- API versioning via headers (not URL)
- Deploy pushed to Friday

Need specific details on any area?
```

### Full Details When Needed
```
User: show me everything about the auth module changes

Assistant: [Detailed code changes, architectural decisions, test results, etc.]
```

## Context Preservation Examples

### Automatic Save on Farewell
```
User: Alright, I'm heading out for the day. See you tomorrow!

Assistant: 👋 Context saved automatically!

**Progress Summary**:
- Payment integration advanced to 75%
- Webhook handler: Signature validation complete
- Tests: All passing (18/18)

**For Tomorrow**:
- Implement retry logic for failed webhooks
- Add comprehensive error handling
- Deploy to staging for integration testing

Have a great evening! Your context is preserved and ready for tomorrow.
```

### Smart Detection of Break
```
User: I need to jump on a call, this might take a while

Assistant: 📝 Auto-saving context before your call...

✅ Context checkpoint created: "pre-call-webhook-implementation"
- Current file positions saved
- Terminal state preserved  
- Memory insights tagged

Take your time! Everything will be here when you return.
```

### Explicit Save Request
```
User: /context save before-refactor

Assistant: ✅ Context saved as "before-refactor"

**Checkpoint includes**:
- Complete project state
- All code positions and changes
- Decision history with rationale
- Current task progress (75%)
- Memory insights and patterns

**Restore command**: `/context restore before-refactor`

This checkpoint will persist even across project switches.
```