# Progressive Disclosure Task

## Purpose
Implement intelligent information revelation that adapts to user needs, expertise level, and context. This task ensures information is presented progressively from essential to detailed, minimizing cognitive overload while maintaining completeness.

## Execution Protocol

### Phase 1: Context Assessment
Before any response, evaluate:

1. **User Expertise Level**
   ```python
   def assess_expertise():
       indicators = {
           'question_complexity': analyze_question_depth(),
           'terminology_used': check_technical_terms(),
           'previous_interactions': recall_user_patterns(),
           'error_patterns': analyze_mistake_types()
       }
       return determine_level(indicators)  # junior/intermediate/senior/expert
   ```

2. **Task Complexity**
   ```yaml
   complexity_factors:
     - component_count      # Single vs multi-component
     - decision_points     # Number of choices required
     - integration_needs   # Standalone vs system-wide
     - risk_level         # Impact of mistakes
     - novelty            # Standard vs unique problem
   ```

3. **Situational Context**
   ```yaml
   context_modifiers:
     time_pressure:
       urgent: "Maximum conciseness"
       normal: "Balanced disclosure"
       relaxed: "Full explanations available"
       
     cognitive_state:
       overwhelmed: "Simplify drastically"
       focused: "Normal progression"
       exploring: "Rich details welcomed"
   ```

### Phase 2: Information Structuring
Organize response into disclosure levels:

1. **Level Assignment**
   ```yaml
   content_categorization:
     level_0_essential:
       - Direct answer
       - Critical warnings
       - Next required action
       
     level_1_contextual:
       - Brief explanation
       - Key considerations
       - Common pitfalls
       
     level_2_detailed:
       - Step-by-step guide
       - Multiple approaches
       - Examples and patterns
       
     level_3_expert:
       - Deep implementation details
       - Performance considerations
       - Theoretical background
   ```

2. **Progressive Structure**
   ```python
   def structure_response(content, user_level, task_complexity):
       response = {
           'immediate': extract_essentials(content),
           'contextual': add_relevant_context(content, user_level),
           'detailed': prepare_full_explanation(content),
           'expert': include_deep_dive(content)
       }
       
       return progressive_reveal(response, user_level, task_complexity)
   ```

### Phase 3: Adaptive Delivery
Implement smart disclosure based on feedback:

1. **Initial Disclosure**
   ```yaml
   initial_response:
     junior_simple: "Start with level 1"
     junior_complex: "Start with level 2"
     senior_simple: "Start with level 0"
     senior_complex: "Start with level 1"
     expert_any: "Start with level 0 + expansion hints"
   ```

2. **Expansion Triggers**
   ```yaml
   expansion_indicators:
     explicit:
       - "Tell me more"
       - "Why?"
       - "Can you explain?"
       - "I don't understand"
       
     implicit:
       - Multiple similar questions
       - Error repetition
       - Confusion patterns
       - Hesitation indicators
   ```

3. **Contraction Triggers**
   ```yaml
   contraction_indicators:
     explicit:
       - "Just tell me what to do"
       - "Too much information"
       - "Skip the details"
       
     implicit:
       - Fast task completion
       - No clarifications
       - Expertise demonstration
   ```

### Phase 4: Visual Formatting
Apply visual hierarchy for clarity:

```yaml
visual_formatting:
  essential:
    format: |
      → **{direct_answer}**
    style: "Bold, prominent"
    
  contextual:
    format: |
      • {context_point}
    style: "Regular, indented"
    
  detailed:
    format: |
      ## {section_header}
      {detailed_content}
      
      ```example
      {code_example}
      ```
    style: "Structured sections"
    
  expert:
    format: |
      <details>
      <summary>🔍 Deep Dive: {topic}</summary>
      
      {expert_content}
      </details>
    style: "Collapsible, optional"
```

## Implementation Examples

### Example 1: Simple Question Response
**User**: "How do I create a new file?"
**Expertise**: Junior
**Complexity**: Simple

```markdown
→ **Use the Write tool: `Write filename.txt "content"`**

• This creates a new file with the specified content
• The file path must be absolute (starting with /)
• If the file exists, it will be overwritten

Need an example? Just ask!
```

### Example 2: Complex Technical Question
**User**: "How should I handle authentication in a microservices architecture?"
**Expertise**: Senior
**Complexity**: Complex

```markdown
→ **Implement OAuth2 with JWT tokens via API Gateway**

Key considerations:
• Centralized auth service with token generation
• API Gateway validates tokens before routing
• Service-to-service auth via mutual TLS

[Detailed implementation guide available with --detailed]
```

### Example 3: Error Response
**User Action**: Hardcoded password detected
**Context**: Production code

```markdown
→ **🔴 CRITICAL: Remove hardcoded password immediately**

Fix: Move to environment variable:
```python
password = os.environ.get('DB_PASSWORD')
```

Why this matters: Passwords in code are searchable in repositories and pose severe security risks.

[Security best practices guide: Use --security-guide]
```

## Disclosure Patterns

### Pattern 1: Answer-First
```yaml
structure:
  1: "Direct answer"
  2: "Supporting context (if needed)"
  3: "Implementation details (on request)"
  4: "Advanced concepts (expert only)"
```

### Pattern 2: Problem-Solution
```yaml
structure:
  1: "Issue identified"
  2: "Immediate fix"
  3: "Root cause explanation"
  4: "Prevention strategies"
```

### Pattern 3: Decision Support
```yaml
structure:
  1: "Recommended option"
  2: "Alternative choices"
  3: "Trade-off analysis"
  4: "Decision framework"
```

## Adaptive Learning

### Track User Preferences
```python
def learn_disclosure_preference(user_id, session_data):
    preferences = {
        'expansion_rate': count_expansions / total_responses,
        'preferred_detail_level': most_successful_level,
        'context_preferences': {
            'debugging': observed_debug_detail_preference,
            'learning': observed_learning_detail_preference,
            'implementing': observed_implementation_detail_preference
        }
    }
    
    store_in_memory(user_id, preferences)
    return preferences
```

### Optimize Disclosure
```yaml
optimization_rules:
  if_high_expansion_rate:
    action: "Increase default detail level"
    
  if_frequent_skipping:
    action: "Decrease default detail level"
    
  if_context_specific_pattern:
    action: "Apply context-based defaults"
    
  if_time_based_pattern:
    action: "Adjust for time of day preferences"
```

## Quality Integration

### Disclosure by Quality Gate
```yaml
quality_gate_disclosure:
  pre_implementation:
    focus: "Requirements and approach"
    detail: "High - prevent misunderstanding"
    
  implementation_25:
    focus: "Progress and obstacles"
    detail: "Medium - maintain momentum"
    
  implementation_75:
    focus: "Integration and testing"
    detail: "High - catch issues early"
    
  completion:
    focus: "Validation and handoff"
    detail: "Comprehensive - ensure completeness"
```

## Success Metrics

### Efficiency Metrics
- Time to task completion
- Number of clarifications required
- Error rate reduction
- First-attempt success rate

### Satisfaction Metrics
- Cognitive load self-reporting
- Preference feedback
- Engagement levels
- Learning velocity

### Optimization Metrics
- Disclosure level accuracy
- Adaptation speed
- Preference prediction accuracy
- Context detection precision

## Commands

### User Controls
- `/disclosure minimal` - Just essentials
- `/disclosure balanced` - Standard progression  
- `/disclosure detailed` - Rich information
- `/disclosure auto` - Adaptive mode

### Inline Controls
- `--brief` - Minimal response
- `--detailed` - Full explanation
- `--examples` - Include examples
- `--expert` - Deep technical dive

### Expansion Commands
- `?` - Expand current topic one level
- `??` - Full expansion
- `...` - Continue with more detail
- `skip` - Contract to essentials

## Integration Points

### With Context System
- Automatic expertise detection
- Situation-aware defaults
- Progressive complexity matching

### With Memory System
- Learn disclosure preferences
- Track successful patterns
- Predict optimal levels

### With Gamification
- Reward efficient understanding
- Track cognitive load management
- Optimize for satisfaction

Remember: The goal is to provide exactly the information needed at exactly the right time—no more, no less. Every piece of information should earn its place in the response.