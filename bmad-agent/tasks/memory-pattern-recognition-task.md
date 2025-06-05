# Memory Pattern Recognition Task

## Purpose
Identify and surface successful patterns from memory to guide current work and prevent repeated mistakes.

## Behavioral Requirements
- **Example-Driven**: Reference patterns from `examples/memory/memory-command-examples.md`
- **Evidence-Based**: All patterns must be backed by actual occurrences
- **Progressive Disclosure**: Start with most relevant patterns, expand on request
- **Actionable Focus**: Every pattern should lead to a specific action or decision

## Pattern Recognition Framework

### Pattern Types

#### 1. Workflow Patterns
Recurring sequences of actions that lead to successful outcomes:
```python
def identify_workflow_patterns(context):
    """Identify successful workflow sequences"""
    patterns = {
        "task_sequences": analyze_task_progression(),
        "persona_transitions": track_handoff_patterns(),
        "decision_chains": map_decision_sequences(),
        "time_patterns": identify_optimal_timing()
    }
    return patterns
```

#### 2. Technical Patterns
Successful technical approaches and architectures:
```python
def identify_technical_patterns(context):
    """Extract reusable technical solutions"""
    patterns = {
        "architecture_decisions": find_successful_architectures(),
        "code_patterns": extract_implementation_patterns(),
        "debugging_approaches": catalog_problem_solutions(),
        "performance_optimizations": track_optimization_patterns()
    }
    return patterns
```

#### 3. Decision Patterns
How decisions are made and their outcomes:
```python
def identify_decision_patterns(context):
    """Analyze decision-making patterns"""
    patterns = {
        "decision_criteria": extract_decision_factors(),
        "stakeholder_alignment": track_consensus_patterns(),
        "risk_mitigation": identify_risk_patterns(),
        "outcome_correlations": map_decision_to_outcome()
    }
    return patterns
```

#### 4. Collaboration Patterns
Successful team interaction and communication patterns:
```python
def identify_collaboration_patterns(context):
    """Track effective collaboration approaches"""
    patterns = {
        "consultation_effectiveness": analyze_consultation_outcomes(),
        "handoff_success": track_handoff_patterns(),
        "communication_styles": identify_effective_styles(),
        "conflict_resolution": catalog_resolution_patterns()
    }
    return patterns
```

#### 5. Quality Patterns
Patterns that lead to high-quality outcomes:
```python
def identify_quality_patterns(context):
    """Extract quality-enhancing patterns"""
    patterns = {
        "testing_strategies": track_test_effectiveness(),
        "review_approaches": analyze_review_outcomes(),
        "documentation_patterns": identify_doc_success(),
        "validation_sequences": map_validation_patterns()
    }
    return patterns
```

## Pattern Recognition Process

### Phase 1: Context Analysis
```python
def analyze_current_context():
    """Understand the current situation deeply"""
    context = {
        "project_type": identify_project_characteristics(),
        "current_phase": determine_project_phase(),
        "active_challenges": list_current_blockers(),
        "team_composition": analyze_team_structure(),
        "technical_stack": catalog_technologies(),
        "constraints": identify_limitations()
    }
    return context
```

### Phase 2: Memory Search
```python
def search_relevant_memories(context):
    """Find memories similar to current context"""
    queries = [
        f"{context.project_type} {context.current_phase} patterns",
        f"solutions for {context.active_challenges}",
        f"{context.technical_stack} best practices",
        f"team of {context.team_composition} success patterns"
    ]
    
    memories = []
    for query in queries:
        results = search_memory(query, limit=10, threshold=0.7)
        memories.extend(results)
    
    return deduplicate_and_rank(memories)
```

### Phase 3: Pattern Extraction
```python
def extract_patterns(memories):
    """Extract patterns from memory collection"""
    patterns = []
    
    # Group memories by similarity
    memory_clusters = cluster_by_similarity(memories)
    
    for cluster in memory_clusters:
        if len(cluster) >= MIN_PATTERN_OCCURRENCES:
            pattern = {
                "type": classify_pattern_type(cluster),
                "description": extract_common_elements(cluster),
                "occurrences": len(cluster),
                "success_rate": calculate_success_rate(cluster),
                "confidence": calculate_confidence_score(cluster),
                "context_similarity": measure_context_match(cluster),
                "key_factors": identify_success_factors(cluster),
                "anti_patterns": extract_failure_modes(cluster)
            }
            patterns.append(pattern)
    
    return patterns
```

### Phase 4: Confidence Scoring
```python
def calculate_pattern_confidence(pattern):
    """Calculate confidence in pattern applicability"""
    
    factors = {
        "occurrence_count": min(pattern.occurrences / 10, 1.0),
        "success_rate": pattern.success_rate,
        "recency": calculate_recency_score(pattern),
        "context_match": pattern.context_similarity,
        "consistency": measure_pattern_consistency(pattern)
    }
    
    weights = {
        "occurrence_count": 0.2,
        "success_rate": 0.3,
        "recency": 0.1,
        "context_match": 0.3,
        "consistency": 0.1
    }
    
    confidence = sum(factors[k] * weights[k] for k in factors)
    return round(confidence * 100)
```

### Phase 5: Pattern Presentation

#### Default View (Concise)
```markdown
🔍 Pattern Analysis: {topic}

📊 Top Pattern (Confidence: 85%)
├─ Type: Workflow Pattern
├─ Success Rate: 92% (12 occurrences)
└─ Key Insight: Start with API design before implementation

⚡ Quick Application:
"Based on this pattern, consider designing your API endpoints before writing any code. This approach succeeded in 11 of 12 similar cases."
```

#### Expanded View (Detailed)
```markdown
🔍 Pattern Analysis: API Development

📊 Pattern 1: API-First Design (Confidence: 85%)
├─ Type: Workflow Pattern
├─ Occurrences: 12 times in similar projects
├─ Success Rate: 92%
├─ Context Match: High (Node.js REST APIs)
│
├─ Success Factors:
│  ├─ Clear endpoint documentation before coding
│  ├─ Early client-server contract agreement
│  └─ Reduced rework from misunderstandings
│
├─ When It Works Best:
│  ├─ Multiple client applications
│  ├─ Distributed team development
│  └─ Clear requirements available
│
└─ Anti-Patterns to Avoid:
   ├─ Starting implementation without API design
   └─ Changing API contract during development

📊 Pattern 2: Incremental Endpoint Development (Confidence: 78%)
[Additional patterns...]
```

## Pattern Application Guidelines

### 1. Context Matching
Before applying a pattern, verify:
- Current context aligns with pattern's success context
- No unique constraints that invalidate the pattern
- Team capability matches pattern requirements

### 2. Adaptation Strategy
```python
def adapt_pattern_to_context(pattern, current_context):
    """Adapt successful pattern to current situation"""
    
    adaptations = []
    
    # Identify differences
    context_delta = compare_contexts(pattern.original_context, current_context)
    
    for difference in context_delta:
        if difference.is_significant():
            adaptation = generate_adaptation(difference, pattern)
            adaptations.append(adaptation)
    
    return {
        "base_pattern": pattern,
        "adaptations": adaptations,
        "confidence_adjustment": calculate_adapted_confidence(adaptations),
        "risks": identify_adaptation_risks(adaptations)
    }
```

### 3. Pattern Evolution
Patterns should evolve based on new experiences:
```python
def update_pattern_effectiveness(pattern_id, outcome):
    """Update pattern based on application outcome"""
    
    pattern = get_pattern(pattern_id)
    
    # Record new occurrence
    pattern.occurrences += 1
    if outcome.successful:
        pattern.successes += 1
    
    # Update success rate
    pattern.success_rate = pattern.successes / pattern.occurrences
    
    # Extract new insights
    if outcome.has_new_insights():
        pattern.insights.extend(outcome.insights)
    
    # Identify new anti-patterns
    if not outcome.successful:
        pattern.anti_patterns.append(outcome.failure_analysis)
    
    save_pattern(pattern)
```

## Anti-Pattern Detection

### Common Anti-Patterns to Flag
1. **Premature Optimization Pattern**
   - Optimizing before establishing baselines
   - Over-engineering for unlikely scenarios

2. **Skip Validation Pattern**
   - Moving to implementation without stakeholder approval
   - Skipping testing phases under time pressure

3. **Solo Hero Pattern**
   - Single person making all decisions
   - Lack of consultation on critical choices

4. **Tech-First Pattern**
   - Choosing technology before understanding requirements
   - Solution looking for a problem

## Integration with Other Systems

### Memory System
- Continuously scan memories for emerging patterns
- Update pattern confidence based on new data
- Create new pattern memories when threshold met

### Quality Framework
- Use patterns to predict quality issues
- Apply quality patterns proactively
- Track pattern impact on quality metrics

### Behavioral Tracking
- Monitor pattern application success
- Track user preference for certain patterns
- Optimize pattern suggestions based on usage

## Error Handling

### No Patterns Found
```markdown
🔍 No established patterns found for current context.

This might be because:
- This is a unique situation
- Not enough historical data
- Context is too specific

Suggestions:
1. Document your approach for future pattern creation
2. Consult with team for similar experiences
3. Start with general best practices
```

### Low Confidence Patterns
```markdown
⚠️ Low Confidence Pattern (45%)

This pattern has limited data:
- Only 3 occurrences
- Mixed success rate (67%)
- Moderate context match

Proceed with caution and consider:
- Adapting significantly for your context
- Having fallback approaches ready
- Documenting outcomes for pattern improvement
```