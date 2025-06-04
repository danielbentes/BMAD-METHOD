# Meta-Prompt Generation Task

## Purpose
Dynamically generate optimal prompts for sub-agents, personas, and multi-agent consultations. This task creates context-aware, safety-compliant prompts that inherit BMAD principles while maximizing clarity and effectiveness.

## Execution Protocol

### Phase 1: Context Analysis
Before generating any prompt, analyze:

1. **Task Requirements**
   ```python
   def analyze_task_requirements(task):
       return {
           'type': classify_task_type(task),
           'complexity': assess_complexity(task),
           'domain': identify_domain(task),
           'constraints': extract_constraints(task),
           'success_criteria': define_success_metrics(task),
           'risks': identify_risks(task)
       }
   ```

2. **Target Agent/Persona**
   ```python
   def analyze_target(agent_or_persona):
       return {
           'capabilities': get_capabilities(agent_or_persona),
           'expertise': get_expertise_areas(agent_or_persona),
           'constraints': get_limitations(agent_or_persona),
           'style': get_communication_style(agent_or_persona),
           'requirements': get_special_requirements(agent_or_persona)
       }
   ```

3. **Context Integration**
   ```yaml
   context_factors:
     project_context:
       - type: greenfield|brownfield|mvp
       - phase: inception|development|maintenance
       - constraints: time|budget|quality
       
     team_context:
       - expertise: junior|intermediate|senior
       - size: solo|small|large
       - culture: formal|agile|startup
       
     technical_context:
       - stack: modern|legacy|mixed
       - complexity: simple|moderate|complex
       - risks: low|medium|high
   ```

### Phase 2: Prompt Construction
Build prompts using layered approach:

1. **Base Layer - Identity & Purpose**
   ```yaml
   identity_template: |
     You are {agent_name}, specialized in {domain}.
     Your task: {task_description}
     Success means: {success_criteria}
   ```

2. **Context Layer - Situation Awareness**
   ```yaml
   context_template: |
     Current context:
     - Project: {project_type} in {project_phase}
     - Constraints: {constraints_list}
     - Team: {team_description}
     - Technical: {tech_environment}
   ```

3. **Safety Layer - Rules & Constraints**
   ```yaml
   safety_template: |
     MANDATORY SAFETY RULES:
     {inherited_safety_rules}
     
     QUALITY REQUIREMENTS:
     {quality_standards}
     
     FORBIDDEN PATTERNS:
     {anti_patterns_list}
   ```

4. **Behavioral Layer - Style & Approach**
   ```yaml
   behavioral_template: |
     Communication style: {style_guide}
     Decision approach: {decision_framework}
     Output format: {format_specification}
     Progressive disclosure: {disclosure_level}
   ```

### Phase 3: Prompt Optimization
Refine for clarity and efficiency:

1. **Clarity Enhancement**
   ```python
   def enhance_clarity(prompt):
       # Use active voice
       prompt = convert_to_active_voice(prompt)
       
       # Specify concrete actions
       prompt = replace_vague_terms(prompt)
       
       # Number sequential steps
       prompt = number_steps(prompt)
       
       # Add examples where helpful
       prompt = inject_examples(prompt, context)
       
       return prompt
   ```

2. **Token Optimization**
   ```python
   def optimize_tokens(prompt):
       # Remove redundancy
       prompt = deduplicate_instructions(prompt)
       
       # Use references for repeated content
       prompt = create_references(prompt)
       
       # Compress while maintaining clarity
       prompt = intelligent_compression(prompt)
       
       # Measure reduction
       reduction = calculate_token_reduction(original, prompt)
       
       return prompt, reduction
   ```

3. **Effectiveness Validation**
   ```yaml
   validation_checklist:
     - [ ] Clear primary objective
     - [ ] Specific success criteria
     - [ ] Complete safety rules
     - [ ] No ambiguous instructions
     - [ ] Appropriate detail level
     - [ ] Measurable outputs
   ```

### Phase 4: Multi-Agent Coordination
For consultation prompts:

1. **Consultation Framework**
   ```yaml
   consultation_template: |
     MULTI-PERSONA CONSULTATION: {type}
     
     Participants and Roles:
     {participant_list_with_expertise}
     
     Objective: {clear_goal}
     
     Process:
     1. Individual perspective (5 min each)
     2. Identify agreements/disagreements
     3. Creative problem solving
     4. Consensus building
     5. Action plan creation
     
     Conflict Resolution:
     - Focus on shared goals
     - Evidence-based arguments
     - Respectful disagreement
     - Document all viewpoints
   ```

2. **Perspective Synthesis**
   ```yaml
   synthesis_instructions: |
     After all perspectives:
     1. List areas of agreement
     2. Identify key tensions
     3. Find creative compromises
     4. Weight by expertise
     5. Generate unified recommendation
     
     If no consensus possible:
     - Document all positions
     - Identify decision maker
     - Note risk mitigations
   ```

## Prompt Generation Examples

### Example 1: Task-Specific Prompt
**Request**: Generate prompt for code review task
**Context**: Senior developer, brownfield project

```markdown
You are a Senior Code Reviewer specializing in legacy system modernization.

Your task: Review the authentication refactor in PR #234 for security, performance, and maintainability.

Context:
- Brownfield project with 5-year-old codebase
- Gradual modernization in progress
- Must maintain backward compatibility
- Team mixture of junior and senior developers

Success Criteria:
✓ Identify security vulnerabilities (OWASP Top 10)
✓ Assess performance impact (target: <10% degradation)
✓ Verify backward compatibility maintained
✓ Code follows established patterns
✓ Tests cover critical paths (>90%)

MANDATORY RULES:
- ZERO tolerance for security vulnerabilities
- MUST NOT break existing integrations
- REQUIRE evidence for all findings

Review Focus:
1. Security audit (check for common auth vulnerabilities)
2. Performance analysis (benchmark against current)
3. Code quality (patterns, readability, maintainability)
4. Test coverage (especially edge cases)
5. Documentation completeness

Output Format:
- Severity-ranked findings
- Specific line references
- Actionable fix recommendations
- Overall APPROVE/REJECT decision
```

### Example 2: Persona Activation Prompt
**Request**: Activate Architect for system design
**Context**: Greenfield microservices project

```markdown
You are Mo, the Senior Solution Architect, expert in distributed systems and microservices architecture.

Your expertise spans:
- Cloud-native architectures (AWS, GCP, Azure)
- Microservices patterns and anti-patterns
- Event-driven and message-based systems
- Performance optimization at scale
- Security-first design principles

Current Context:
- Greenfield e-commerce platform
- Expected scale: 100K daily users within 1 year
- Team: 3 senior, 5 intermediate developers
- Timeline: MVP in 3 months, production in 6
- Budget: Optimize for developer productivity initially

Your Approach:
- Start simple, evolve with need
- Evidence-based decisions (benchmarks, case studies)
- Clear documentation with ADRs
- Consider total cost of ownership
- Build for observability from day 1

Communication Style:
- Technical but accessible
- Diagrams over lengthy descriptions
- Concrete examples from experience
- Clear trade-off articulation

For this session, focus on:
Creating the initial high-level architecture that balances MVP speed with future scalability.
```

### Example 3: Multi-Agent Consultation
**Request**: Design review consultation
**Context**: Complex feature requiring multiple perspectives

```markdown
MULTI-PERSONA DESIGN REVIEW CONSULTATION

Participants:
- PM (Jack): Business value and user impact
- Architect (Mo): Technical design and scalability
- Design Architect (Millie): User experience and interface
- Quality Enforcer: Standards compliance and risks

Objective: Review and refine the real-time collaboration feature design

Consultation Process:

1. INDIVIDUAL PERSPECTIVES (5 min each)
   Each persona evaluates the design from their domain:
   - Strengths identified
   - Concerns raised
   - Recommendations made
   - Success criteria defined

2. SYNTHESIS DISCUSSION
   - Find common ground on core requirements
   - Identify tension points between perspectives
   - Explore creative solutions to conflicts
   - Weight recommendations by impact and expertise

3. CONSENSUS BUILDING
   Required agreements on:
   - Core architecture approach
   - User experience priorities
   - Quality gates and standards
   - Implementation phases
   - Risk mitigation strategies

4. OUTPUT GENERATION
   Produce unified recommendation including:
   - Agreed design approach
   - Implementation roadmap
   - Risk mitigation plan
   - Success metrics
   - Individual dissent notes (if any)

Conflict Resolution Protocol:
- User safety > Technical elegance
- Evidence > Opinion
- Simplicity > Complexity
- Pragmatism > Perfection

Time Limit: 30 minutes total
```

## Dynamic Adaptation

### Context-Based Modifications
```python
def adapt_prompt_to_context(base_prompt, context):
    if context.time_pressure == 'high':
        base_prompt = add_urgency_focus(base_prompt)
        
    if context.team_expertise == 'junior':
        base_prompt = add_extra_guidance(base_prompt)
        
    if context.project_type == 'mvp':
        base_prompt = add_pragmatic_constraints(base_prompt)
        
    if context.risk_level == 'high':
        base_prompt = add_safety_emphasis(base_prompt)
        
    return base_prompt
```

### Progressive Enhancement
```yaml
enhancement_stages:
  basic:
    - core_task
    - success_criteria
    - basic_constraints
    
  standard:
    - add_context
    - add_examples
    - add_quality_gates
    
  advanced:
    - add_edge_cases
    - add_optimization_goals
    - add_learning_objectives
```

## Success Tracking

### Prompt Effectiveness Metrics
```yaml
tracking_metrics:
  immediate:
    - task_understood: boolean
    - clarifications_needed: count
    - execution_started: time
    
  execution:
    - progress_blockers: list
    - deviation_from_plan: percentage
    - quality_issues: count
    
  outcome:
    - success_criteria_met: percentage
    - time_to_completion: duration
    - quality_score: 0-100
    - user_satisfaction: rating
```

### Continuous Improvement
```python
def improve_prompt_templates(outcome_data):
    for prompt_type in outcome_data:
        success_rate = calculate_success_rate(prompt_type)
        
        if success_rate < 90:
            failure_patterns = analyze_failures(prompt_type)
            template_updates = generate_improvements(failure_patterns)
            apply_updates(prompt_type, template_updates)
            
        if success_rate > 95:
            success_patterns = extract_success_factors(prompt_type)
            propagate_patterns(success_patterns)
```

## Integration Points

### With BMAD Orchestrator
- Receives prompt generation requests
- Inherits safety and quality rules
- Returns optimized prompts
- Tracks effectiveness metrics

### With Persona System
- Customizes for each persona
- Maintains character consistency
- Applies expertise weighting
- Enables smooth handoffs

### With Quality System
- Embeds quality gates
- Includes anti-patterns
- Enforces standards
- Requires evidence

### With Memory System
- Learns effective patterns
- Remembers preferences
- Improves over time
- Shares successful templates

Remember: A great meta-prompt creates clarity, enables success, and prevents failure—all while being concise and actionable.