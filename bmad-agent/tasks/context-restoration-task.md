# Context Restoration Task

## Purpose
Enable seamless work continuation across contexts with intelligent restoration and change awareness.

## Behavioral Requirements
- **Example-Driven**: Reference patterns from `examples/continuity/context-restoration-examples.md`
- **Progressive Disclosure**: Start with essential summary, expand on request
- **Memory Integration**: Leverage past restoration patterns for optimization
- **User-Centric**: Focus on what matters to the user, not technical details

## Context Restoration Process

### 1. Auto-Detection Phase
When user returns or starts new conversation:

```python
def detect_context_continuation():
    """Detect if this is a continuation of previous work"""
    
    indicators = {
        "has_previous_context": check_context_exists(),
        "time_since_last": calculate_time_gap(),
        "user_greeting": analyze_initial_message(),
        "project_match": verify_project_continuity()
    }
    
    if indicators["has_previous_context"] and indicators["time_since_last"] < 24_hours:
        return RestorationType.QUICK_RESUME
    elif indicators["has_previous_context"] and indicators["project_match"]:
        return RestorationType.FULL_RESTORE
    else:
        return RestorationType.FRESH_START
```

### 2. Quick Restoration (< 2 hours gap)
For short breaks, provide minimal context:

```markdown
🔄 Welcome back! Continuing from 45 minutes ago...

**Last activity**: Implementing payment gateway integration
**Progress**: 65% complete

Ready to continue? Type /continue or start with your question.
```

### 3. Full Restoration (2-24 hours gap)
For longer breaks, provide comprehensive summary:

```markdown
# 🔄 Welcome Back!

## Last Context Summary
**When**: 3 hours ago
**Duration**: 2.5 hours
**Active Persona**: Developer (Jonsey)
**Last Activity**: Payment gateway integration

## What's Changed Since You Left
📝 **New commits** (by others):
- Fix: Resolved CORS issue in API endpoints
- Feature: Added rate limiting to auth endpoints

🔔 **Team updates**:
- QA reported issue with user registration flow
- Design team uploaded new mockups for checkout

💡 **Memory Insights**:
- Similar payment integrations typically need webhook security
- Consider implementing idempotency keys (pattern from 3 past projects)

## Continue Where You Left Off?
- [x] Resume: Payment gateway integration (65% complete)
- [ ] Address: QA-reported registration issue
- [ ] Review: New checkout mockups

Type `/continue` to resume or choose a priority above.
```

### 4. Extended Gap Restoration (>24 hours)
For extended absences, provide strategic overview:

```markdown
# 🔄 Project Context Restoration

## Time Away: 3 days

## Project Status Overview
**Sprint Progress**: Day 8 of 14
**Overall Progress**: 42% → 58% (+16%)

## Key Developments While Away
1. **Completed by team**:
   - User authentication module
   - Database migration scripts
   - CI/CD pipeline setup

2. **New Priorities**:
   - Payment integration (your work) - blocking
   - Performance optimization - high priority
   - Security audit prep - medium priority

3. **Decisions Made**:
   - Switched from REST to GraphQL for admin API
   - Adopted Redis for session management
   - Moved deployment target to K8s

## Recommended Next Steps
Based on current priorities and your past work:
1. Complete payment integration (est. 4 hours)
2. Review GraphQL migration impact
3. Update your local environment for Redis

Would you like a detailed briefing on any area?
```

### 5. Context Restoration with Conflicts
When the current state conflicts with saved context:

```markdown
⚠️ Context Restoration Notice

**Saved context**: Working on feature-auth branch
**Current state**: On main branch with uncommitted changes

## Conflict Resolution Options:
1. Stash current changes and switch to feature-auth
2. Commit current work and merge contexts
3. Keep current state and update context

What would you like to do? (1/2/3)
```

## Smart Continuation Features

### 1. Contextual Command Shortcuts
Based on restored context, offer relevant shortcuts:

```markdown
⚡ Quick Actions (based on your context):
- `/continue payment` - Resume payment integration
- `/test payment` - Run payment module tests  
- `/review changes` - See what changed while away
- `/sync team` - Get team updates
```

### 2. Proactive Alerts
Surface important changes immediately:

```markdown
🚨 Important Updates:
- Breaking API change in auth service (affects your work)
- New security requirement for payment handling
- Deadline moved up by 2 days
```

### 3. Memory-Enhanced Suggestions
Use memory to predict needs:

```markdown
💡 Based on similar situations:
- You typically review test coverage after payment integrations
- Consider security audit checklist (you used it 3 times before)
- Watch for webhook timeout issues (common pattern detected)
```

## Multi-Project Context Management

### Project Switching
When user works on multiple projects:

```markdown
🔄 Project Context Available:

1. **E-Commerce API** (current)
   - Last: 2 hours ago
   - State: Payment integration 65%
   
2. **Analytics Dashboard**
   - Last: Yesterday
   - State: Chart component refactoring
   
3. **Mobile App**
   - Last: 3 days ago
   - State: Push notification setup

Switch to: /context restore [project-name]
```

### Context Isolation
Keep project contexts separate:

```python
def restore_project_context(project_name):
    """Restore specific project context"""
    
    # Clear current context
    clear_active_context()
    
    # Load project-specific context
    context = load_context(f".bmad/projects/{project_name}/context-state.md")
    
    # Load project-specific memories
    memories = load_project_memories(project_name)
    
    # Apply project preferences
    apply_project_settings(context.preferences)
    
    return context
```

## Context Summary Generation

### Automatic Summaries
Generate concise summaries for different purposes:

1. **End-of-Session Summary**:
```markdown
📝 Session Summary - {timestamp}

**Duration**: 2.5 hours
**Completed**: 
- ✅ Payment gateway integration (base)
- ✅ Webhook endpoint setup
- ✅ Initial test suite

**Decisions**:
- Use Stripe for payment processing
- Implement webhook signature validation
- Add idempotency keys for safety

**Next Session**:
- Complete webhook security
- Add comprehensive error handling
- Deploy to staging for testing
```

2. **Handoff Summary**:
```markdown
🤝 Context Summary for Handoff

**Current State**: Payment module 65% complete
**Blockers**: Need Stripe API keys for testing
**Critical Info**: Webhook URL must be whitelisted
**Next Steps**: See payment-integration.md for details
```

## Progressive Disclosure Levels

### Level 0 (Default)
- 2-4 lines maximum
- Current state + next action
- Time since last activity

### Level 1 ("tell me more")
- Include recent changes
- Show team updates
- List available contexts

### Level 2 ("full details")
- Complete activity history
- All decisions with rationale
- Comprehensive change log
- Memory insights and patterns

## Error Handling

### Missing Context
```markdown
🔍 No previous context found.

Would you like to:
1. Start fresh with a new project
2. Search for contexts in other locations
3. Bootstrap from existing codebase

Choose option or describe your project:
```

### Corrupted Context
```markdown
⚠️ Context restoration issue detected.

✅ Partial recovery successful:
- Project configuration restored
- Recent decisions recovered

❌ Could not restore:
- Task progress metrics
- Some memory associations

Recommended: Continue with partial context or start fresh?
```

## Integration Points

### Memory System
- Query restoration patterns for optimization
- Store successful restoration approaches
- Learn from restoration failures

### Quality Framework  
- Validate restored context integrity
- Ensure continuity meets quality standards
- Check for security in restored credentials

### Behavioral Tracking
- Track restoration success rates
- Monitor context switch patterns
- Optimize based on user behavior