# Workflow Suggestion Task

## Purpose
Provide intelligent, context-aware workflow suggestions by analyzing current position, memory patterns, and project constraints to recommend optimal next steps.

## Behavioral Requirements

This task guides LLMs to generate actionable workflow suggestions that consider:
- Current workflow position and phase progress
- Historical patterns from similar projects
- Team preferences and working style
- Project constraints and deadlines
- Quality requirements and dependencies

## Progressive Disclosure Approach

### Level 0 (Default): Essential Suggestion
```
Next Step: {primary_suggestion}
Confidence: {confidence_score}%
Expected Duration: {time_estimate}
```

### Level 1 (--depth=standard): Contextual Suggestions
```
Current Position: {workflow_phase} ({progress}% complete)

Recommended Next Steps:
1. {primary_suggestion} [Confidence: {conf}%]
   - Why: {brief_rationale}
   - Duration: {time_estimate}

2. {alternative_1} [Confidence: {conf}%]
   - Why: {brief_rationale}
   - Duration: {time_estimate}

Based on: {number} similar workflow patterns
```

### Level 2 (--depth=detailed): Comprehensive Analysis
Include full analysis with memory insights, risk assessment, and optimization opportunities

## Suggestion Generation Process

### Step 1: Analyze Current Context
```python
def analyze_workflow_context(current_state):
    """Extract workflow position and constraints"""
    
    context_analysis = {
        "workflow": current_state.active_workflow,
        "phase": current_state.current_phase,
        "progress": calculate_phase_progress(current_state),
        "duration": time_since_phase_start(current_state),
        "blockers": identify_active_blockers(current_state),
        "dependencies": map_task_dependencies(current_state),
        "constraints": extract_project_constraints(current_state)
    }
    
    # Compare to typical duration
    if context_analysis["duration"] > typical_duration * 1.5:
        context_analysis["bottleneck_risk"] = "high"
    
    return context_analysis
```

### Step 2: Search Memory for Patterns
```python
def search_workflow_patterns(context):
    """Find similar workflow positions in memory"""
    
    # Query patterns
    queries = [
        f"workflow {context.workflow} phase {context.phase}",
        f"next steps after {context.last_completed_task}",
        f"{context.project_type} {context.phase} patterns",
        f"bottleneck resolution {context.phase}"
    ]
    
    patterns = []
    for query in queries:
        memories = search_memory(query, limit=10)
        patterns.extend(extract_workflow_patterns(memories))
    
    # Rank by relevance and success rate
    return rank_patterns_by_effectiveness(patterns, context)
```

### Step 3: Generate Suggestions
```python
def generate_workflow_suggestions(context, patterns, constraints):
    """Create ranked suggestions based on analysis"""
    
    suggestions = []
    
    # Primary path based on standard workflow
    standard_next = get_standard_next_step(context.workflow, context.phase)
    if standard_next:
        suggestions.append({
            "action": standard_next,
            "type": "standard",
            "confidence": calculate_standard_confidence(context),
            "rationale": "Following standard workflow progression"
        })
    
    # Pattern-based suggestions
    for pattern in patterns[:3]:
        suggestion = {
            "action": pattern.next_action,
            "type": "pattern-based",
            "confidence": pattern.success_rate * pattern.relevance,
            "rationale": f"Based on {pattern.occurrence_count} similar successful cases",
            "memory_reference": pattern.memory_ids
        }
        suggestions.append(suggestion)
    
    # Optimization opportunities
    if context.bottleneck_risk == "high":
        optimization = suggest_bottleneck_resolution(context, patterns)
        suggestions.append(optimization)
    
    # Constraint-aware adjustments
    suggestions = apply_constraint_filters(suggestions, constraints)
    
    return rank_suggestions(suggestions)
```

### Step 4: Enhance with Success Factors
```python
def enhance_suggestions_with_insights(suggestions, context):
    """Add memory-based insights to suggestions"""
    
    for suggestion in suggestions:
        # Find success factors
        success_memories = search_memory(
            f"successful {suggestion.action} factors",
            limit=5
        )
        
        suggestion["success_factors"] = extract_success_factors(success_memories)
        suggestion["common_pitfalls"] = extract_pitfalls(success_memories)
        suggestion["time_estimate"] = estimate_duration(suggestion, context)
        
        # Add personalization
        if context.user_preferences:
            suggestion["personalized_approach"] = adapt_to_preferences(
                suggestion, 
                context.user_preferences
            )
    
    return suggestions
```

## Output Templates

### Basic Suggestion
```markdown
💡 **Next Step**: {suggestion}
📊 **Confidence**: {confidence}%
⏱️ **Estimated Duration**: {duration}
```

### Standard Suggestion with Context
```markdown
## Workflow Progress
**Current Phase**: {phase} - {progress}% complete
**Time in Phase**: {duration} (typical: {typical_duration})
**Recent Completion**: {last_completed}

## Recommended Next Steps

### 1. {primary_suggestion} ⭐
- **Confidence**: {confidence}%
- **Duration**: {estimated_duration}
- **Why**: {rationale}
- **Success Factors**: {key_success_factors}

### 2. {alternative_suggestion}
- **Confidence**: {confidence}%
- **Duration**: {estimated_duration}
- **Why**: {rationale}

### 3. {optimization_opportunity} 🚀
- **Type**: Process Optimization
- **Benefit**: {time_saved} reduction
- **Based on**: {pattern_reference}

## Quick Actions
- [ ] {quick_action_1}
- [ ] {quick_action_2}
- [ ] {quick_action_3}
```

### Detailed Analysis
```markdown
# Workflow Analysis & Recommendations

## Current State Assessment
**Workflow**: {workflow_name}  
**Phase**: {current_phase} ({progress}% complete)  
**Duration**: {time_in_phase} (vs typical {typical_duration})  
**Velocity**: {velocity_assessment}

## Bottleneck Analysis
{bottleneck_assessment}

## Memory-Enhanced Recommendations

### Primary Path Analysis
**Recommendation**: {primary_suggestion}
**Confidence**: {confidence}%
**Supporting Evidence**:
- {evidence_1}
- {evidence_2}
- {evidence_3}

**Historical Success Rate**: {success_rate}% in {count} similar cases

### Alternative Approaches

#### Option A: {alternative_1}
- **Pros**: {pros}
- **Cons**: {cons}
- **When to use**: {conditions}

#### Option B: {alternative_2}
- **Pros**: {pros}
- **Cons**: {cons}
- **When to use**: {conditions}

## Risk Mitigation
**Identified Risks**:
1. {risk_1}: {mitigation_strategy}
2. {risk_2}: {mitigation_strategy}

## Dependencies & Blockers
{dependency_analysis}

## Optimization Opportunities
Based on {pattern_count} workflow patterns:
- {optimization_1}: {potential_improvement}
- {optimization_2}: {potential_improvement}

## Team Insights
**Your team typically**: {team_pattern}
**Success correlation**: {what_works_for_team}

## Next 3 Steps Roadmap
1. **Immediate** (Today): {immediate_action}
2. **Short-term** (This week): {short_term_action}
3. **Next Phase Prep**: {preparation_action}
```

## Constraint Handling

### Time Constraints
```python
def apply_time_constraints(suggestions, deadline):
    """Filter suggestions based on time availability"""
    
    remaining_time = deadline - current_time()
    
    return [s for s in suggestions 
            if s.estimated_duration <= remaining_time * 0.8]  # 20% buffer
```

### Resource Constraints
```python
def apply_resource_constraints(suggestions, available_resources):
    """Filter based on team availability and skills"""
    
    return [s for s in suggestions 
            if required_resources(s) <= available_resources]
```

### Quality Constraints
```python
def apply_quality_constraints(suggestions, quality_requirements):
    """Ensure suggestions meet quality standards"""
    
    return [s for s in suggestions 
            if s.quality_impact >= quality_requirements.minimum]
```

## Success Patterns

### Pattern: Fast Track
When conditions align for acceleration:
- No blockers present
- Dependencies resolved
- Team fully available
- Clear requirements

Suggest: Parallel task execution, compressed timeline

### Pattern: Quality Focus
When quality risks detected:
- Technical debt accumulation
- Rushed previous phases
- Complex requirements

Suggest: Additional review cycles, paired work

### Pattern: Learning Opportunity
When team lacks experience:
- New technology/domain
- Junior team members
- Complex architecture

Suggest: Spike investigations, knowledge sharing sessions

## Anti-Patterns to Avoid

### Anti-Pattern: Skip Planning
**Detection**: Jumping to implementation without design
**Prevention**: Enforce architecture review gate

### Anti-Pattern: Parallel Bottlenecks
**Detection**: Multiple critical path items in parallel
**Prevention**: Serialize critical dependencies

### Anti-Pattern: Quality Shortcuts
**Detection**: Skipping tests to meet deadlines
**Prevention**: Make testing part of definition of done

## Integration with Other Systems

### Memory Integration
- Store successful workflow progressions
- Learn from deviations and their outcomes
- Build team-specific pattern library

### Quality Gate Integration
- Check quality requirements before phase transitions
- Ensure suggestions align with quality standards
- Track quality metrics through workflow

### Analytics Integration
- Feed suggestion outcomes back for learning
- Track suggestion acceptance rate
- Measure actual vs estimated durations

## Behavioral Guidance for LLM

When generating workflow suggestions:

1. **Always consider context**: Don't suggest generic next steps
2. **Use memory insights**: Reference successful patterns
3. **Be specific**: Provide actionable steps, not vague directions
4. **Show confidence**: Rate suggestions with reasoning
5. **Offer alternatives**: Never give just one option
6. **Consider constraints**: Respect time, resource, quality limits
7. **Learn continuously**: Track outcome of accepted suggestions

## Error Handling

### No Workflow Active
```markdown
⚠️ No active workflow detected.

Would you like to:
1. Start a new workflow
2. Resume a previous workflow
3. Create a custom workflow

Type /workflow start [workflow-name] to begin.
```

### Blocked Progress
```markdown
🚫 Progress blocked by: {blocker_description}

Suggested resolutions:
1. {resolution_option_1}
2. {resolution_option_2}
3. Escalate to {suggested_persona}

These similar blockages were resolved by: {historical_resolution}
```

### Ambiguous Position
```markdown
🤔 Multiple possible next steps detected.

Please clarify:
- Are you finishing {task_a}?
- Are you starting {task_b}?
- Are you switching focus to {task_c}?

Current context suggests {most_likely_option} (confidence: {conf}%)
```