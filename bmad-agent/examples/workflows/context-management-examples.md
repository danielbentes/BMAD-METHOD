# Context Management Examples

## Good Examples ✅

### Example 1: Clean Context Display
**Scenario**: User requests current context
```
User: /context

Assistant: 📍 Project: E-Commerce API | Phase: Development | Active: 3 hours

🎯 Current Focus
└─ Implementing payment gateway integration

📊 Recent Decisions (Last 3)
├─ ✅ Stripe API: Selected for payment processing
├─ ✅ Webhook security: HMAC validation required
└─ ⏳ Rate limiting: Evaluating token bucket vs sliding window

💡 Memory Insights
└─ Similar projects used token bucket successfully (87% confidence)

⚡ Quick Actions
├─ /continue - Resume payment integration
├─ /patterns payment - See payment patterns
└─ /handoff architect - Architecture review
```

### Example 2: Context Save with Meaningful Name
**Scenario**: User saves context before major change
```
User: /context save pre-refactor

Assistant: ✅ Context saved as "pre-refactor"
Checkpoint includes:
- Project state and configuration
- 12 decisions tracked
- Active work: Payment gateway integration
- Memory insights preserved
```

### Example 3: Context Restore with Change Summary
**Scenario**: User restores previous context
```
User: /context restore pre-refactor

Assistant: 🔄 Context restored from "pre-refactor"

📅 Checkpoint from: 2 hours ago
Time elapsed: 2 hours 15 minutes

🔍 What's Changed Since:
- Completed user authentication endpoints
- Added 3 new API routes
- Resolved CORS configuration issue

💡 Suggested Next Steps:
1. Review refactoring requirements
2. Run tests to ensure stability
3. Create new checkpoint before proceeding
```

### Example 4: Natural Language Context Search
**Scenario**: User searches for past decisions
```
User: /context search "database choice"

Assistant: 🔍 Context Search: "database choice"

Found 3 relevant matches:

1. 📅 2 days ago - Architecture Decision
   └─ "Selected PostgreSQL for primary data store"
   💡 Insight: Decision based on ACID compliance needs

2. 📅 1 day ago - Performance Optimization
   └─ "Added Redis for caching layer"
   💡 Insight: Reduced database load by 60%

3. 📅 4 hours ago - Schema Design
   └─ "Implemented soft deletes for audit trail"
   💡 Insight: Maintains data history for compliance
```

## Bad Examples ❌

### Example 1: Exposing Technical Identifiers
**Wrong**:
```
User: /context

Assistant: Session ID: abc-123-def-456
Session State File: /Users/dev/.bmad/state/context-state.md
Memory Provider: OpenMemory MCP v1.2.3
...
```

**Why it's wrong**: Exposes technical details users shouldn't see

### Example 2: Ambiguous Context Information
**Wrong**:
```
User: /context

Assistant: I think you're working on some API stuff.
Maybe you made some decisions about databases?
The project seems to be going okay.
```

**Why it's wrong**: Uses "I think", lacks specific information, no evidence

### Example 3: Missing Memory Integration
**Wrong**:
```
User: /context

Assistant: Current project: E-Commerce API
Phase: Development
No historical data available.
```

**Why it's wrong**: Doesn't leverage memory for insights

## Progressive Disclosure Examples

### Level 0 (Default - Concise)
```
User: /context

Assistant: 📍 E-Commerce API | Development | 3 hours active
🎯 Payment gateway integration (65% complete)
💡 Token bucket pattern recommended for rate limiting
⚡ /continue to resume or /suggest for next steps
```

### Level 1 (Expanded)
```
User: tell me more

Assistant: 
📊 Detailed Context:

Project Details:
- Type: REST API with Node.js/Express
- Database: PostgreSQL + Redis cache
- Auth: JWT with refresh tokens

Recent Progress:
- ✅ User authentication complete
- ✅ Product CRUD endpoints tested
- 🔄 Payment integration in progress
- ⏳ Order management pending

Key Decisions:
1. Stripe for payments (PCI compliance)
2. Token bucket for rate limiting (scalability)
3. Soft deletes for audit trails (compliance)

Team Insights:
- Last handoff: From Architect to Dev (2 hours ago)
- Quality gate: Passed at 50% milestone
```

### Level 2 (Comprehensive)
```
User: show complete context

Assistant: [Full detailed context with complete history, all decisions, full memory associations, etc.]
```

## Context Search Examples

### Searching Decisions
```
User: /context search "why did we choose"

Assistant: Shows all decisions with rationale
```

### Searching by Time
```
User: /context search "yesterday's progress"

Assistant: Shows time-filtered results
```

### Searching by Persona
```
User: /context search "architect recommendations"

Assistant: Shows architect-specific context
```

## Error Handling Examples

### No Context Found
```
User: /context

Assistant: 🔍 No active context found.

Would you like to:
1. Start fresh with /init
2. Restore a checkpoint with /context restore
3. Bootstrap from existing code with /bootstrap-memory
```

### Corrupted Context Recovery
```
User: /context

Assistant: ⚠️ Context integrity issue detected.

Attempting recovery...
✅ Partial context recovered

Missing elements:
- Recent decision history
- Task progress metrics

Recommended: /bootstrap-memory to rebuild context
```