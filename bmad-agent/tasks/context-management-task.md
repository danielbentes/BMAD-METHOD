# Context Management Task

## Purpose
Provide unified context management that abstracts technical details while maintaining rich contextual awareness.

## Behavioral Requirements
- **Example-Driven**: Reference patterns from `examples/workflows/context-management-examples.md`
- **No Technical IDs**: Never expose session IDs, internal references, or technical identifiers
- **Progressive Disclosure**: Essential information first, expand on user request
- **Memory Integration**: Seamlessly incorporate relevant memory insights

## Context Operations

### Display Context
When user invokes `/context` without parameters:

1. **Gather Current State**
   - Load context from `.bmad/state/context-state.md`
   - Check current persona, active tasks, and project phase
   - Identify recent decisions and their rationale
   - Note any active blockers or concerns

2. **Enhance with Memory**
   - Search memory for relevant patterns: `{project-type} successful patterns`
   - Query recent insights: `insights from last {timeframe}`
   - Identify applicable lessons learned

3. **Format Display**
   Use context visualization format:
   ```
   📍 Project: {name} | Phase: {phase} | Active: {duration}
   
   🎯 Current Focus
   └─ {primary_task_or_concern}
   
   📊 Recent Decisions (Last 3)
   ├─ ✅ {decision_1}: {brief_rationale}
   ├─ ✅ {decision_2}: {brief_rationale}
   └─ ⏳ {pending_decision}: {status}
   
   💡 Memory Insights
   └─ {most_relevant_pattern_or_suggestion}
   
   ⚡ Quick Actions
   ├─ /continue - Resume last task
   ├─ /suggest - Get recommendations
   └─ /handoff {persona} - Switch with context
   ```

### Save Context
When user invokes `/context save [name]`:

1. **Capture Comprehensive State**
   - Current project configuration
   - Active persona and task
   - All major decisions with rationale
   - Current blockers and concerns
   - Recent memory insights applied

2. **Create Checkpoint**
   - Generate timestamp
   - Assign user-friendly name (or auto-generate if not provided)
   - Store in `.bmad/state/checkpoints/{name}.md`
   - Update checkpoint index

3. **Confirm Save**
   ```
   ✅ Context saved as "{name}"
   Checkpoint includes:
   - Project state and configuration
   - {count} decisions tracked
   - Active work: {current_task}
   - Memory insights preserved
   ```

### Restore Context
When user invokes `/context restore [name]`:

1. **Load Checkpoint**
   - Retrieve from `.bmad/state/checkpoints/{name}.md`
   - Validate checkpoint integrity
   - Check for compatibility

2. **Restore State**
   - Update current context state
   - Reload project configuration
   - Restore persona and task state
   - Re-apply relevant memory context

3. **Brief on Changes**
   ```
   🔄 Context restored from "{name}"
   
   📅 Checkpoint from: {timestamp}
   Time elapsed: {duration}
   
   🔍 What's Changed Since:
   - {change_1}
   - {change_2}
   
   💡 Suggested Next Steps:
   1. {suggestion_based_on_restored_context}
   ```

### Search Context
When user invokes `/context search {query}`:

1. **Natural Language Search**
   - Parse query intent
   - Search across:
     - Current context state
     - Saved checkpoints
     - Decision history
     - Task completions
     - Memory insights applied

2. **Rank Results**
   - Relevance to query
   - Recency weighting
   - Impact significance
   - Context similarity to current state

3. **Present Findings**
   ```
   🔍 Context Search: "{query}"
   
   Found {count} relevant matches:
   
   1. 📅 {date} - {context_type}
      └─ {relevant_excerpt}
      💡 Insight: {why_this_matters}
   
   2. 📅 {date} - {context_type}
      └─ {relevant_excerpt}
      💡 Insight: {why_this_matters}
   ```

## Anti-Patterns to Avoid
- ❌ Never show: "Session ID: abc123" or similar technical identifiers
- ❌ Avoid: "Loading session state..." (use "Gathering context...")
- ❌ Don't expose: File paths or internal references
- ❌ Never say: "I think the context might be..." (use evidence)

## Success Patterns
- ✅ Natural language: "Your project is in the development phase"
- ✅ User-friendly: "Last checkpoint: 2 hours ago"
- ✅ Actionable: "Based on your context, consider..."
- ✅ Memory-enhanced: "Similar projects succeeded with..."

## Error Handling

### Missing Context
If no context exists:
```
🔍 No active context found.

Would you like to:
1. Start fresh with /init
2. Restore a checkpoint with /context restore
3. Bootstrap from existing code with /bootstrap-memory
```

### Corrupted Context
If context is unreadable:
```
⚠️ Context integrity issue detected.

Attempting recovery...
✅ Partial context recovered

Missing elements:
- {missing_element_1}
- {missing_element_2}

Recommended: /bootstrap-memory to rebuild context
```

## Progressive Disclosure Levels

### Level 0 (Default)
Show only essential context (4-6 lines)

### Level 1 (--full flag or "tell me more")
Include:
- Extended decision history
- Detailed memory insights
- Full task progression
- Team collaboration context

### Level 2 ("show everything" or "complete context")
Comprehensive dump including:
- All checkpoints
- Complete decision tree
- Full memory associations
- Historical patterns

## Integration Points

### Memory System
- Auto-query relevant memories for context enhancement
- Store significant context changes as memories
- Use memory patterns to predict next actions

### Quality Framework
- Ensure context operations meet quality standards
- Validate checkpoint integrity
- Enforce progressive disclosure

### Behavioral Tracking
- Track context management effectiveness
- Monitor checkpoint usage patterns
- Optimize based on user preferences