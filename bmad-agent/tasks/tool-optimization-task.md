# Tool Optimization Task

## Purpose
Analyze current tool usage patterns and optimize for efficiency, context preservation, and task success. This task monitors tool selection, identifies inefficiencies, and suggests improvements based on the tool preference hierarchy.

## Execution Protocol

### Phase 1: Tool Usage Analysis
1. **Current Session Analysis**
   - Track all tool invocations
   - Measure execution time per tool
   - Calculate context token usage
   - Identify success/failure patterns

2. **Pattern Recognition**
   - Sequential vs parallel opportunities
   - Redundant tool usage
   - Inefficient tool choices
   - Context overflow risks

3. **Performance Metrics**
   ```yaml
   metrics_collected:
     - tool_name
     - execution_time
     - context_tokens_used
     - success_rate
     - error_frequency
     - user_satisfaction
   ```

### Phase 2: Optimization Recommendations
Based on analysis, provide specific recommendations:

1. **Tool Substitutions**
   - Replace forbidden tools with preferred alternatives
   - Upgrade to more efficient tools
   - Suggest tool combinations

2. **Execution Improvements**
   - Identify parallelization opportunities
   - Recommend batching strategies
   - Suggest tool chaining patterns

3. **Context Optimization**
   - Recommend token-saving approaches
   - Suggest aggregation strategies
   - Identify unnecessary reads

### Phase 3: Implementation Guidance
Provide actionable steps to implement optimizations:

```yaml
optimization_report:
  current_inefficiencies:
    - issue: "Sequential file edits"
      impact: "3x slower execution"
      solution: "Use MultiEdit for batch changes"
      example: |
        # Current (inefficient)
        Edit file.py "old1" "new1"
        Edit file.py "old2" "new2"
        
        # Optimized
        MultiEdit file.py [
          {"old": "old1", "new": "new1"},
          {"old": "old2", "new": "new2"}
        ]
        
  parallel_opportunities:
    - current: "Sequential git status, then npm test"
      optimized: "Parallel execution in single call"
      time_saved: "~3 seconds"
      
  tool_preferences:
    - forbidden_tool_used: "find command"
      replacement: "Glob tool"
      reason: "10x faster, better pattern support"
```

## Tool Preference Enforcement

### Forbidden Tools Detection
```python
forbidden_patterns = {
    'find': 'Use Glob instead',
    'grep': 'Use Grep tool instead',
    'cat': 'Use Read tool instead',
    'sed': 'Use Edit instead',
    'awk': 'Use MultiEdit instead'
}

def check_tool_usage(command):
    for forbidden, alternative in forbidden_patterns.items():
        if forbidden in command:
            return f"FORBIDDEN: {forbidden} detected. {alternative}"
    return None
```

### Efficiency Scoring
```yaml
efficiency_score:
  calculation:
    - parallel_usage: 30%
    - tool_selection: 30%
    - context_efficiency: 20%
    - execution_speed: 20%
    
  thresholds:
    excellent: >90%
    good: 70-90%
    needs_improvement: 50-70%
    poor: <50%
```

## Context-Specific Optimizations

### By Project Type
```yaml
greenfield_optimizations:
  emphasis: "Exploration and research"
  preferred_tools: [WebSearch, Task, Glob]
  avoid: "Premature optimization"
  
brownfield_optimizations:
  emphasis: "Safety and compatibility"
  preferred_tools: [Grep, Read, Edit]
  avoid: "Broad changes without analysis"
  
mvp_optimizations:
  emphasis: "Speed and essentials"
  preferred_tools: [MultiEdit, Write]
  avoid: "Over-tooling"
```

### By Task Type
```yaml
debugging_optimizations:
  sequence: "Diagnose → Analyze → Fix → Verify"
  tools: [mcp__ide__getDiagnostics, Grep, Read, Edit]
  parallel: false  # Sequential for cause-effect
  
refactoring_optimizations:
  sequence: "Find → Plan → Execute → Test"
  tools: [Glob, Task, MultiEdit, Bash]
  parallel: true   # Maximize efficiency
  
implementation_optimizations:
  sequence: "Understand → Code → Test → Document"
  tools: [Read, MultiEdit, Bash, Write]
  parallel: "Test while coding"
```

## Learning and Adaptation

### Success Pattern Storage
When optimizations succeed:
1. Document the pattern
2. Store in memory with context
3. Calculate improvement metrics
4. Add to preference database

### Failure Analysis
When tools fail:
1. Identify root cause
2. Document failure pattern
3. Update fallback strategies
4. Adjust preferences if needed

## Output Format
```yaml
tool_optimization_report:
  session_analysis:
    total_tool_calls: 47
    inefficient_patterns: 12
    optimization_opportunities: 8
    estimated_time_savings: "15 minutes"
    
  top_recommendations:
    1:
      issue: "Sequential file edits"
      solution: "Use MultiEdit"
      impact: "70% faster"
      
    2:
      issue: "Redundant file reads"
      solution: "Read once, cache content"
      impact: "Save 2000 tokens"
      
    3:
      issue: "Shell grep usage"
      solution: "Use Grep tool"
      impact: "10x faster search"
      
  implementation_priority:
    high: "Fix forbidden tool usage"
    medium: "Implement parallel execution"
    low: "Optimize tool sequences"
```

## Integration Points
- Runs automatically when inefficiency detected
- Can be triggered manually via `/optimize-tools`
- Results feed into tool preference learning
- Updates stored in memory for future sessions

## Success Criteria
- 90% reduction in forbidden tool usage
- 50% improvement in execution time
- 30% reduction in context token usage
- Zero tool-related failures