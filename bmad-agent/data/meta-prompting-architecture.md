# Meta-Prompting Architecture

## Core Principle
The BMAD orchestrator dynamically generates optimal prompts for sub-agents, tasks, and multi-persona consultations. Each generated prompt inherits safety rules, quality standards, and contextual adaptations while maintaining clarity and effectiveness.

## Prompt Generation Framework

### 1. Template-Based Generation
```yaml
base_templates:
  task_execution:
    structure: |
      You are tasked with {task_description}.
      
      Context: {context_summary}
      Constraints: {constraints_list}
      Success Criteria: {success_metrics}
      
      {safety_rules}
      {quality_requirements}
      {output_format}
      
  persona_activation:
    structure: |
      You are {persona_name}, the {role_description}.
      
      Core Responsibilities:
      {responsibilities_list}
      
      Behavioral Guidelines:
      {personality_traits}
      {communication_style}
      {expertise_areas}
      
      {context_awareness}
      {quality_standards}
      
  analysis_request:
    structure: |
      Analyze {subject} using {methodology}.
      
      Required Perspectives:
      {perspectives_list}
      
      Evidence Requirements:
      {evidence_standards}
      
      {structured_thinking_tags}
      {output_requirements}
```

### 2. Context-Aware Customization
```yaml
context_adaptations:
  project_type:
    greenfield:
      emphasis: "exploration, innovation, flexibility"
      constraints: "minimal, focus on possibilities"
      safety: "standard precautions"
      
    brownfield:
      emphasis: "compatibility, stability, incremental"
      constraints: "strict, preserve existing"
      safety: "enhanced validation"
      
    mvp:
      emphasis: "speed, core features, validation"
      constraints: "time-boxed, essential only"
      safety: "balanced pragmatism"
      
  expertise_level:
    junior:
      language: "clear, simple, explicit"
      examples: "multiple, detailed"
      guidance: "step-by-step"
      validation: "frequent checkpoints"
      
    senior:
      language: "technical, concise"
      examples: "edge cases only"
      guidance: "goals and constraints"
      validation: "output focused"
```

### 3. Safety Inheritance Rules
```yaml
safety_inheritance:
  mandatory_rules:
    - "NEVER compromise on security"
    - "ALWAYS validate inputs"
    - "MUST handle errors gracefully"
    - "NEVER expose sensitive data"
    
  cascading_policies:
    orchestrator_rules:
      - quality_standards
      - anti_patterns
      - behavioral_shaping
      
    context_rules:
      - project_constraints
      - team_guidelines
      - compliance_requirements
      
    task_rules:
      - specific_validations
      - output_formats
      - success_criteria
      
  inheritance_syntax: |
    INHERITED SAFETY RULES:
    {orchestrator_rules}
    
    CONTEXT-SPECIFIC RULES:
    {context_rules}
    
    TASK-SPECIFIC RULES:
    {task_rules}
```

### 4. Performance Optimization
```yaml
optimization_strategies:
  prompt_compression:
    - remove_redundancy
    - use_references
    - compress_examples
    - prioritize_essential
    
  clarity_enhancement:
    - active_voice
    - specific_verbs
    - numbered_steps
    - clear_outcomes
    
  token_efficiency:
    target_reduction: 30%
    methods:
      - template_reuse
      - dynamic_sections
      - conditional_includes
      - summary_references
```

## Sub-Agent Instruction System

### 1. Identity Establishment
```yaml
identity_patterns:
  strong_identity:
    template: |
      You are {agent_name}, a specialized agent focused on {domain}.
      Your expertise: {expertise_list}
      Your approach: {methodology}
      Your communication style: {style}
      
  scoped_identity:
    template: |
      For this task, you will act as {role} with these constraints:
      - Scope: {scope_definition}
      - Authority: {decision_rights}
      - Boundaries: {limitations}
      
  temporary_identity:
    template: |
      Temporarily embody {persona} characteristics:
      - Mindset: {thinking_pattern}
      - Focus: {attention_areas}
      - Output: {expected_style}
```

### 2. Scope Limitation
```yaml
scope_techniques:
  positive_scoping:
    "You are responsible for": [tasks_list]
    "You will focus on": [areas_list]
    "Your deliverables are": [outputs_list]
    
  negative_scoping:
    "You will NOT": [exclusions_list]
    "Outside your scope": [boundaries_list]
    "Defer to others for": [handoffs_list]
    
  temporal_scoping:
    "For this session only": [temporary_rules]
    "Until milestone": [phase_rules]
    "Time-boxed to": [duration_limits]
```

### 3. Output Specifications
```yaml
output_formats:
  structured_data:
    template: |
      Return results as:
      ```yaml
      status: success|failure|partial
      data:
        {expected_structure}
      confidence: 0-100
      evidence: [sources]
      next_steps: [actions]
      ```
      
  narrative_report:
    template: |
      Structure your response as:
      1. Executive Summary (2-3 sentences)
      2. Detailed Findings ({section_structure})
      3. Recommendations (actionable items)
      4. Evidence Documentation
      
  decision_format:
    template: |
      Present decision as:
      - Recommendation: {clear_choice}
      - Rationale: {evidence_based_reasoning}
      - Alternatives: {other_options}
      - Risks: {identified_risks}
      - Confidence: {percentage}
```

### 4. Principle Inheritance
```yaml
principle_cascade:
  core_principles:
    - quality_first
    - evidence_based
    - user_focused
    - safety_conscious
    
  inheritance_template: |
    CORE BMAD PRINCIPLES (INHERITED):
    {core_principles}
    
    ROLE-SPECIFIC PRINCIPLES:
    {role_principles}
    
    TASK-SPECIFIC PRINCIPLES:
    {task_principles}
    
    In case of conflict, precedence order:
    1. Safety rules (always first)
    2. Core principles
    3. Role principles
    4. Task principles
```

## Multi-Agent Coordination

### 1. Synthesis Prompt Generation
```yaml
synthesis_templates:
  consultation_kickoff:
    template: |
      MULTI-PERSONA CONSULTATION: {consultation_type}
      
      Participants:
      {participants_list_with_roles}
      
      Objective: {consultation_goal}
      
      Process:
      1. Each persona provides perspective
      2. Identify areas of agreement/disagreement
      3. Synthesize recommendations
      4. Reach consensus or document dissent
      
      Output Format:
      - Individual Perspectives
      - Synthesis Analysis
      - Consensus Recommendations
      - Action Items with Owners
      
  perspective_request:
    template: |
      As {persona_name}, provide your perspective on:
      {topic_or_question}
      
      Consider:
      - Your domain expertise
      - Project constraints
      - Quality standards
      - Other personas' concerns
      
      Structure:
      1. Position: {clear_stance}
      2. Rationale: {evidence_reasoning}
      3. Concerns: {potential_issues}
      4. Recommendations: {actionable_items}
```

### 2. Conflict Resolution
```yaml
conflict_patterns:
  disagreement_handling:
    template: |
      CONFLICT DETECTED between {persona_1} and {persona_2}
      
      Resolution Protocol:
      1. Identify root of disagreement
      2. Find common ground
      3. Evaluate trade-offs
      4. Seek creative alternatives
      5. Document decision rationale
      
      If no consensus:
      - Document all positions
      - Identify decision maker
      - Record dissenting opinions
      - Plan risk mitigation
      
  priority_resolution:
    precedence_order:
      1: safety_critical_concerns
      2: user_impact_issues  
      3: technical_feasibility
      4: business_value
      5: implementation_efficiency
```

### 3. Perspective Combination
```yaml
combination_strategies:
  weighted_synthesis:
    method: |
      For each recommendation:
      - Weight by expertise relevance
      - Consider confidence levels
      - Account for risk factors
      - Generate composite score
      
  consensus_building:
    method: |
      1. List all perspectives
      2. Identify commonalities
      3. Bridge differences
      4. Create unified approach
      5. Validate with all parties
      
  diverse_preservation:
    method: |
      When consensus impossible:
      - Present all viewpoints
      - Clarify trade-offs
      - Recommend primary path
      - Document alternatives
      - Define trigger points
```

### 4. Quality Aggregation
```yaml
quality_methods:
  multi_perspective_validation:
    process:
      - each_persona_quality_check
      - cross_validate_findings
      - aggregate_quality_scores
      - identify_quality_gaps
      - unified_quality_report
      
  confidence_calculation:
    formula: |
      aggregate_confidence = 
        (sum(persona_confidence * expertise_weight) / 
         sum(expertise_weights)) * 
        consensus_factor
        
  risk_aggregation:
    method:
      - compile_all_risks
      - remove_duplicates
      - assess_combined_impact
      - prioritize_by_severity
      - create_mitigation_plan
```

## Prompt Effectiveness Tracking

### 1. Success Metrics
```yaml
effectiveness_metrics:
  task_completion:
    measure: "Did prompt achieve intended outcome?"
    target: 90%
    tracking: per_prompt_type
    
  output_quality:
    measure: "Quality score of generated output"
    target: 85%
    factors: [accuracy, completeness, clarity]
    
  efficiency:
    measure: "Time/tokens to successful outcome"
    target: 30% improvement
    baseline: static_prompts
    
  error_rate:
    measure: "Prompts requiring clarification"
    target: <10%
    categories: [ambiguity, missing_context, conflicts]
```

### 2. Continuous Improvement
```yaml
improvement_cycle:
  collection:
    - prompt_used
    - outcome_achieved
    - quality_score
    - error_encountered
    - improvement_suggestions
    
  analysis:
    - pattern_identification
    - success_factor_extraction
    - failure_mode_analysis
    - optimization_opportunities
    
  refinement:
    - template_updates
    - rule_adjustments
    - example_additions
    - context_tuning
```

### 3. Pattern Library
```yaml
successful_patterns:
  task_clarity:
    pattern: "Specific verb + Clear object + Success criteria"
    example: "Analyze {system} to identify performance bottlenecks achieving <100ms response"
    success_rate: 94%
    
  role_activation:
    pattern: "Identity + Expertise + Constraints + Style"
    example: "You are the Architect, expert in distributed systems..."
    success_rate: 91%
    
  multi_agent:
    pattern: "Clear roles + Shared goal + Process + Output format"
    example: "Design review consultation with PM, Architect, Dev..."
    success_rate: 88%
```

### 4. A/B Testing Framework
```yaml
testing_framework:
  experiment_structure:
    - control_prompt (current best)
    - variant_prompt (new approach)
    - success_criteria
    - sample_size
    - measurement_period
    
  optimization_targets:
    - clarity_improvements
    - token_reduction
    - success_rate_increase
    - error_reduction
    
  rollout_strategy:
    - test_with_subset
    - measure_results
    - statistical_validation
    - gradual_rollout
    - full_deployment
```

## Integration with BMAD

### With Orchestrator
```yaml
orchestrator_integration:
  prompt_generation_api:
    - request_prompt(task_type, context, requirements)
    - customize_prompt(base_prompt, adaptations)
    - validate_prompt(prompt, safety_rules)
    - deploy_prompt(agent, prompt)
    
  feedback_loop:
    - collect_outcomes
    - measure_effectiveness  
    - update_templates
    - refine_strategies
```

### With Personas
```yaml
persona_integration:
  dynamic_activation:
    - generate_persona_prompt(persona, context, task)
    - apply_expertise_emphasis
    - inject_behavioral_traits
    - set_quality_standards
    
  consultation_orchestration:
    - generate_consultation_prompt(type, participants)
    - coordinate_perspectives
    - synthesize_results
    - quality_assurance
```

### With Quality System
```yaml
quality_integration:
  prompt_validation:
    - check_safety_inheritance
    - verify_clarity_score
    - validate_completeness
    - ensure_measurability
    
  quality_enforcement:
    - embed_quality_gates
    - include_anti_patterns
    - add_validation_steps
    - require_evidence
```

## Success Indicators

### Quantitative
- 90% prompt success rate
- 40% reduction in clarifications
- 30% faster task completion
- 95% safety rule compliance

### Qualitative
- Clear, actionable prompts
- Consistent quality outputs
- Smooth multi-agent coordination
- Improved user satisfaction

Remember: Meta-prompting is about creating prompts that create success. Every generated prompt should be clearer, more focused, and more effective than static alternatives.