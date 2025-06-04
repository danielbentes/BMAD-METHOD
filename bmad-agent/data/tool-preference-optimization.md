# Tool Preference Optimization System

## Core Principle
Guide AI tool selection toward optimal patterns through clear hierarchies, forbidden patterns, and performance-based learning. Every tool choice should maximize efficiency while maintaining safety and quality.

## Tool Preference Hierarchies

### 1. Search Operations
```yaml
search_hierarchy:
  forbidden:
    - find: "File system traversal - use Glob instead"
    - grep: "Shell grep - use Grep tool instead"
    - cat: "Raw file reading - use Read tool instead"
    - head: "Partial file reading - use Read with limits"
    - tail: "File end reading - use Read with offset"
    - ls: "Directory listing - use LS tool instead"
    
  primary_tools:
    complex_search:
      1: Task  # For multi-file, complex pattern searches
      2: Agent # For open-ended exploration
      
    code_search:
      1: Grep  # For content pattern matching
      2: Task  # If Grep insufficient
      
    file_search:
      1: Glob  # For filename patterns
      2: LS    # For directory exploration
      
    specific_read:
      1: Read  # For known file paths
      2: NotebookRead # For .ipynb files
      
  performance_notes:
    - "Task tool for complex searches reduces context usage"
    - "Grep 10x faster than shell grep for large codebases"
    - "Glob handles patterns better than manual traversal"
    - "Read with offset/limit prevents context overflow"
```

### 2. File Operations
```yaml
file_hierarchy:
  forbidden:
    - vim: "Interactive editing - use Edit/MultiEdit"
    - nano: "Interactive editing - use Edit/MultiEdit"
    - sed: "Stream editing - use Edit with patterns"
    - awk: "Text processing - use Edit/MultiEdit"
    
  primary_tools:
    single_change:
      1: Edit  # For one change in one file
      
    multiple_changes:
      1: MultiEdit # For multiple changes in same file
      2: Edit      # Fallback if MultiEdit fails
      
    new_file:
      1: Write # For creating new files
      2: MultiEdit # For create + immediate edits
      
    notebook_edit:
      1: NotebookEdit # For .ipynb files only
      
  efficiency_patterns:
    - "MultiEdit reduces tool calls by 70% for refactoring"
    - "Batch related changes in single MultiEdit call"
    - "Read before Edit to ensure context"
    - "Prefer Edit over Write for existing files"
```

### 3. Analysis Operations
```yaml
analysis_hierarchy:
  forbidden:
    - "Manual pattern counting": "Use analysis tools"
    - "Visual inspection only": "Use structured analysis"
    
  primary_tools:
    memory_operations:
      1: memory-operations-task # For complex memory work
      2: TodoRead/TodoWrite     # For task tracking
      
    code_analysis:
      1: mcp__ide__getDiagnostics # For IDE diagnostics
      2: structured_analysis_tags  # For decisions
      
    web_research:
      1: WebSearch # For current information
      2: WebFetch  # For specific pages
      
  context_specific:
    greenfield_project:
      emphasis: "Research and exploration tools"
      preferred: [WebSearch, Task, memory-operations-task]
      
    debugging_context:
      emphasis: "Diagnostic and analysis tools"
      preferred: [mcp__ide__getDiagnostics, Grep, Read]
      
    refactoring_context:
      emphasis: "Efficient multi-edit tools"
      preferred: [MultiEdit, Glob, Task]
```

### 4. Execution Operations
```yaml
execution_hierarchy:
  forbidden:
    - "cd && command": "Use absolute paths instead"
    - "Interactive commands": "No user input possible"
    
  primary_tools:
    shell_operations:
      1: Bash # For all command execution
      conditions:
        - "Quote paths with spaces"
        - "Use ; or && for multiple commands"
        - "Avoid cd, use absolute paths"
        
    python_execution:
      1: mcp__ide__executeCode # For notebook contexts
      2: Bash with python      # For scripts
      
  parallel_execution:
    pattern: "Multiple independent operations"
    approach: "Single message, multiple tool calls"
    benefit: "50% faster execution, better UX"
```

## Anti-Tool Patterns

### 1. Forbidden Tool Uses
```yaml
critical_violations:
  - pattern: "Using find command"
    penalty: -$1000
    reason: "Inefficient, use Glob tool"
    alternative: "Glob with pattern"
    
  - pattern: "Shell grep instead of Grep tool"
    penalty: -$1000
    reason: "Slower, less features"
    alternative: "Grep tool with regex"
    
  - pattern: "Multiple cd commands"
    penalty: -$500
    reason: "State management issues"
    alternative: "Absolute paths"
    
  - pattern: "Interactive editors"
    penalty: -$2000
    reason: "No user interaction possible"
    alternative: "Edit/MultiEdit tools"
```

### 2. Common Misuse Patterns
```yaml
inefficient_patterns:
  sequential_edits:
    detection: "Multiple Edit calls to same file"
    impact: "3x slower, more context"
    correction: "Use MultiEdit for batch changes"
    example: |
      # BAD: Sequential edits
      Edit file.py "old1" "new1"
      Edit file.py "old2" "new2"
      Edit file.py "old3" "new3"
      
      # GOOD: Batch with MultiEdit
      MultiEdit file.py [
        {"old": "old1", "new": "new1"},
        {"old": "old2", "new": "new2"},
        {"old": "old3", "new": "new3"}
      ]
      
  redundant_reads:
    detection: "Reading same file multiple times"
    impact: "Wastes context tokens"
    correction: "Read once, reference content"
    
  exploratory_bash:
    detection: "Using ls, find, grep in Bash"
    impact: "Inefficient exploration"
    correction: "Use specialized tools"
```

### 3. Performance Penalties
```yaml
penalty_matrix:
  tool_misuse:
    wrong_tool_choice: -$500
    forbidden_tool_use: -$1000
    inefficient_pattern: -$750
    repeated_inefficiency: -$1500
    
  performance_impact:
    minor_slowdown: -$250      # <2x slower
    moderate_slowdown: -$500   # 2-5x slower
    major_slowdown: -$1000     # >5x slower
    context_overflow: -$2000   # Causes token issues
```

## Tool Combination Patterns

### 1. Optimal Sequences
```yaml
search_and_edit:
  pattern: "Find files → Read content → Edit matches"
  sequence:
    1: Glob "**/*.py"        # Find Python files
    2: Grep "TODO"           # Search for TODOs
    3: Read [matched files]  # Read full context
    4: MultiEdit [files]     # Fix all TODOs
  efficiency: "75% faster than manual search"
  
refactoring_flow:
  pattern: "Analyze → Plan → Execute → Verify"
  sequence:
    1: Task "analyze dependencies"
    2: structured_analysis_tag
    3: MultiEdit [all changes]
    4: mcp__ide__getDiagnostics
  efficiency: "Reduces errors by 90%"
  
research_flow:
  pattern: "Web search → Analyze → Document"
  sequence:
    1: WebSearch "topic"
    2: WebFetch [relevant URLs]
    3: memory-operations-task "store insights"
    4: Write "research-summary.md"
```

### 2. Parallel Execution
```yaml
parallel_patterns:
  independent_checks:
    use_case: "Multiple status checks"
    approach: "Execute git status, npm test, file reads in parallel"
    benefit: "3x faster than sequential"
    
  multi_file_read:
    use_case: "Reading multiple files"
    approach: "Batch all Read operations"
    benefit: "Single round trip"
    
  comprehensive_search:
    use_case: "Complex search across codebase"
    approach: "Glob + Grep + Read in parallel"
    benefit: "5x faster search completion"
```

### 3. Tool Output Chaining
```yaml
chaining_patterns:
  search_modify_verify:
    chain: "Grep → Read → MultiEdit → Validate"
    data_flow: "Match list → Content → Changes → Verification"
    
  analyze_decide_implement:
    chain: "Task → Analysis Tag → Implementation → Test"
    data_flow: "Research → Decision → Code → Validation"
    
  memory_enhanced_flow:
    chain: "Recall → Analyze → Update → Remember"
    data_flow: "Past patterns → Current analysis → Action → New learning"
```

## Adaptive Tool Selection

### 1. Learning Patterns
```yaml
success_tracking:
  pattern_database:
    - context: "large refactoring"
      tools_used: [Task, Glob, MultiEdit]
      success_rate: 92%
      time_saved: "3 hours"
      
    - context: "bug investigation"
      tools_used: [Grep, Read, mcp__ide__getDiagnostics]
      success_rate: 87%
      issues_found: "within 5 minutes"
      
    - context: "new feature"
      tools_used: [WebSearch, Task, Write, MultiEdit]
      success_rate: 95%
      quality_score: "high"
```

### 2. Context-Aware Selection
```yaml
context_rules:
  debugging:
    primary: [mcp__ide__getDiagnostics, Grep, Read]
    avoid: [Write, MultiEdit until cause found]
    
  refactoring:
    primary: [Glob, MultiEdit, Task]
    parallel: true
    batch_size: "maximize"
    
  research:
    primary: [WebSearch, WebFetch, memory-operations]
    avoid: [premature implementation]
    
  implementation:
    primary: [Read, MultiEdit, Bash for tests]
    sequence: "understand → implement → verify"
```

### 3. Performance Monitoring
```yaml
metrics:
  tool_efficiency:
    track:
      - execution_time
      - success_rate
      - context_usage
      - user_satisfaction
      
  optimization_triggers:
    slow_execution: "Switch to parallel"
    high_failure: "Add validation step"
    context_overflow: "Use Task aggregation"
    repeated_use: "Consider batching"
```

### 4. Automatic Optimization
```yaml
optimization_rules:
  - trigger: "Same file edited 3+ times"
    action: "Suggest MultiEdit batching"
    
  - trigger: "Sequential searches taking >30s"
    action: "Switch to Task tool"
    
  - trigger: "Context >80% full"
    action: "Aggregate with Task, use summaries"
    
  - trigger: "Tool failures >2 in row"
    action: "Fallback to alternative tool"
```

## Tool Preference Integration

### With Configuration
```yaml
tool_preferences:
  search_operations:
    forbidden: [find, grep, cat, head, tail, ls]
    preferred:
      1: Task (for complex searches)
      2: Grep (for code search)
      3: Glob (for file patterns)
      4: Read (for specific files)
```

### With Personas
Each persona has tool preferences:
- **Analyst**: WebSearch, Task, memory-operations
- **Architect**: Glob, Read, MultiEdit for diagrams
- **Developer**: MultiEdit, Bash, mcp__ide__getDiagnostics
- **Quality**: Grep for violations, Task for analysis

### With Context System
- **Junior context**: More Read operations, sequential execution
- **Senior context**: Parallel operations, Task aggregation
- **MVP context**: Minimal tool use, fast execution
- **Enterprise**: Comprehensive tooling, full validation

## Success Metrics

### Quantitative
- 90% optimal tool selection rate
- 30% reduction in execution time
- 50% fewer context overflows
- 80% reduction in tool failures

### Qualitative
- Clear tool selection rationale
- Predictable performance
- Reduced user frustration
- Improved task completion

## Common Pitfalls

### 1. Over-Tooling
- **Problem**: Using complex tools for simple tasks
- **Solution**: Start simple, escalate if needed
- **Example**: Read before Task for single file

### 2. Sequential Syndrome
- **Problem**: Not leveraging parallel execution
- **Solution**: Identify independent operations
- **Example**: Batch all file reads together

### 3. Context Explosion
- **Problem**: Tools returning too much data
- **Solution**: Use limits, offsets, summaries
- **Example**: Read with line limits for large files

### 4. Tool Lock-In
- **Problem**: Always using same tool
- **Solution**: Consider context and alternatives
- **Example**: Task vs Grep based on search complexity

## Implementation Checklist

- [ ] Check forbidden tools list before execution
- [ ] Consider parallel execution opportunities
- [ ] Evaluate context usage before tool choice
- [ ] Learn from successful patterns
- [ ] Monitor performance metrics
- [ ] Adapt based on context
- [ ] Document new patterns discovered

Remember: The best tool is the one that completes the task efficiently while preserving context and maintaining quality. When in doubt, refer to the preference hierarchy and let performance guide evolution.