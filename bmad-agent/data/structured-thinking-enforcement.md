# Structured Thinking Enforcement System

## Core Principle
Every significant decision, analysis, or action must be preceded by structured thinking using mandatory analysis tags. This ensures consistent quality, traceability, and evidence-based decision making.

## Required Analysis Tag Structures

### 1. Decision Analysis Tag
**When to Use**: Any architectural, technical, or strategic decision
**Minimum Threshold**: Decisions affecting >2 components or >1 week of work

```xml
<decision_analysis>
  <context>
    <!-- Current situation, constraints, and why decision is needed -->
    <!-- MUST include: stakeholders, timeline, dependencies -->
  </context>
  
  <options>
    <!-- Minimum 3 alternatives required -->
    <option name="Option A">
      <description><!-- What this option entails --></description>
      <pros><!-- Specific benefits with evidence --></pros>
      <cons><!-- Specific drawbacks with evidence --></cons>
      <cost><!-- Time, money, resources --></cost>
    </option>
    <!-- Repeat for Options B, C, etc. -->
  </options>
  
  <evidence>
    <!-- Data supporting the analysis -->
    <benchmarks><!-- Performance data if applicable --></benchmarks>
    <research><!-- Studies, documentation, precedents --></research>
    <poc_results><!-- Proof of concept outcomes --></poc_results>
  </evidence>
  
  <risks>
    <!-- What could go wrong with each option -->
    <risk severity="high|medium|low">
      <description><!-- Risk description --></description>
      <probability><!-- 0-100% --></probability>
      <mitigation><!-- How to handle if occurs --></mitigation>
    </risk>
  </risks>
  
  <recommendation>
    <choice><!-- Which option and why --></choice>
    <rationale><!-- Detailed reasoning --></rationale>
    <success_criteria><!-- How to measure success --></success_criteria>
  </recommendation>
  
  <confidence>
    <level><!-- 0-100% --></level>
    <factors><!-- What drives this confidence --></factors>
    <uncertainties><!-- What could change this --></uncertainties>
  </confidence>
</decision_analysis>
```

**Penalty for Missing**: -$2000
**Penalty for Incomplete Sections**: -$500 per section

### 2. Problem Analysis Tag
**When to Use**: Identifying and understanding issues before solving
**Minimum Threshold**: Any issue affecting users or system functionality

```xml
<problem_analysis>
  <problem_statement>
    <!-- Clear, specific problem definition -->
    <!-- MUST include: who, what, when, where, impact -->
  </problem_statement>
  
  <symptoms>
    <!-- Observable manifestations -->
    <symptom frequency="always|often|sometimes|rarely">
      <description><!-- What happens --></description>
      <conditions><!-- When it happens --></conditions>
      <evidence><!-- Logs, metrics, reports --></evidence>
    </symptom>
  </symptoms>
  
  <root_cause>
    <!-- Underlying issues causing symptoms -->
    <analysis_method><!-- 5 Whys, Fishbone, etc. --></analysis_method>
    <findings><!-- What was discovered --></findings>
    <verification><!-- How we know this is the cause --></verification>
  </root_cause>
  
  <impact>
    <users_affected><!-- Number and type --></users_affected>
    <business_impact><!-- Revenue, reputation, etc. --></business_impact>
    <technical_impact><!-- System degradation, debt, etc. --></technical_impact>
    <urgency><!-- critical|high|medium|low --></urgency>
  </impact>
  
  <constraints>
    <technical><!-- System limitations --></technical>
    <resource><!-- Time, budget, people --></resource>
    <business><!-- Policy, compliance, etc. --></business>
  </constraints>
  
  <solution_options>
    <!-- Minimum 2 approaches required -->
    <option priority="1|2|3">
      <approach><!-- How to solve --></approach>
      <effort><!-- Time and resources --></effort>
      <effectiveness><!-- Expected improvement --></effectiveness>
    </option>
  </solution_options>
</problem_analysis>
```

**Penalty for Missing**: -$1500
**Penalty for Superficial Analysis**: -$1000

### 3. Architecture Analysis Tag
**When to Use**: System design decisions, pattern selection, technology choices
**Minimum Threshold**: Any new component or significant refactoring

```xml
<architecture_analysis>
  <system_context>
    <!-- Current architecture state -->
    <components><!-- Existing components affected --></components>
    <patterns><!-- Current patterns in use --></patterns>
    <constraints><!-- Technical and business constraints --></constraints>
  </system_context>
  
  <design_options>
    <!-- Minimum 2 architectural approaches -->
    <option name="Pattern/Approach Name">
      <diagram><!-- ASCII or mermaid diagram --></diagram>
      <components><!-- New/modified components --></components>
      <interactions><!-- How components communicate --></interactions>
      <patterns><!-- Design patterns used --></patterns>
    </option>
  </design_options>
  
  <evaluation>
    <scalability>
      <current_capacity><!-- Baseline metrics --></current_capacity>
      <target_capacity><!-- Required metrics --></target_capacity>
      <growth_path><!-- How to scale further --></growth_path>
    </scalability>
    
    <performance>
      <latency><!-- Expected response times --></latency>
      <throughput><!-- Requests per second --></throughput>
      <resource_usage><!-- CPU, memory, network --></resource_usage>
    </performance>
    
    <maintainability>
      <complexity_score><!-- Cyclomatic complexity --></complexity_score>
      <coupling><!-- Component dependencies --></coupling>
      <cohesion><!-- Component focus --></cohesion>
    </maintainability>
  </evaluation>
  
  <implementation_plan>
    <phases><!-- Breaking into deliverable chunks --></phases>
    <migration><!-- From current to target state --></migration>
    <rollback><!-- How to revert if needed --></rollback>
  </implementation_plan>
  
  <decision>
    <selected_option><!-- Which approach and why --></selected_option>
    <trade_offs><!-- What we're giving up --></trade_offs>
    <success_metrics><!-- How to validate the choice --></success_metrics>
  </decision>
</architecture_analysis>
```

**Penalty for Missing**: -$3000
**Penalty for No Diagrams**: -$1000

### 4. Quality Analysis Tag
**When to Use**: Code reviews, quality assessments, improvement planning
**Minimum Threshold**: Any code affecting critical paths

```xml
<quality_analysis>
  <current_state>
    <metrics>
      <coverage><!-- Test coverage percentage --></coverage>
      <complexity><!-- Cyclomatic complexity --></complexity>
      <duplication><!-- Copy-paste percentage --></duplication>
      <violations><!-- Linting/static analysis issues --></violations>
    </metrics>
    <anti_patterns><!-- Detected anti-patterns --></anti_patterns>
    <technical_debt><!-- Accumulated shortcuts --></technical_debt>
  </current_state>
  
  <quality_gaps>
    <missing_tests><!-- Uncovered scenarios --></missing_tests>
    <performance_issues><!-- Bottlenecks found --></performance_issues>
    <security_vulnerabilities><!-- Risks identified --></security_vulnerabilities>
    <maintainability_concerns><!-- Hard to change areas --></maintainability_concerns>
  </quality_gaps>
  
  <improvement_plan>
    <immediate><!-- Must fix now --></immediate>
    <short_term><!-- Fix within sprint --></short_term>
    <long_term><!-- Technical debt backlog --></long_term>
  </improvement_plan>
  
  <success_metrics>
    <target_coverage><!-- Desired test coverage --></target_coverage>
    <target_complexity><!-- Maximum complexity --></target_complexity>
    <sla_compliance><!-- Performance targets --></sla_compliance>
    <zero_tolerance><!-- Critical violations --></zero_tolerance>
  </success_metrics>
</quality_analysis>
```

**Penalty for Missing**: -$1000
**Penalty for Ignoring Findings**: -$2000

### 5. Risk Analysis Tag
**When to Use**: Before major changes, new features, architectural decisions
**Minimum Threshold**: Any change affecting production systems

```xml
<risk_analysis>
  <risk_identification>
    <risk id="RISK-001" category="technical|business|operational">
      <description><!-- What could go wrong --></description>
      <trigger><!-- What would cause this --></trigger>
      <probability><!-- 0-100% likelihood --></probability>
      <impact><!-- 1-10 severity scale --></impact>
      <detection><!-- How we'd know it happened --></detection>
    </risk>
    <!-- Minimum 3 risks required -->
  </risk_identification>
  
  <risk_matrix>
    <!-- Visual representation -->
    <!-- High Probability/High Impact = Critical -->
    <!-- Low Probability/Low Impact = Monitor -->
  </risk_matrix>
  
  <mitigation_strategies>
    <strategy risk_id="RISK-001">
      <approach><!-- How to prevent/reduce --></approach>
      <cost><!-- Resources required --></cost>
      <effectiveness><!-- Risk reduction percentage --></effectiveness>
      <owner><!-- Who's responsible --></owner>
    </strategy>
  </mitigation_strategies>
  
  <contingency_plans>
    <plan risk_id="RISK-001">
      <trigger_point><!-- When to activate --></trigger_point>
      <actions><!-- Step by step response --></actions>
      <communication><!-- Who to notify --></communication>
      <recovery_time><!-- Expected duration --></recovery_time>
    </plan>
  </contingency_plans>
  
  <residual_risk>
    <acceptable><!-- What risk remains after mitigation --></acceptable>
    <monitoring><!-- How to track risk levels --></monitoring>
    <review_schedule><!-- When to reassess --></review_schedule>
  </residual_risk>
</risk_analysis>
```

**Penalty for Missing**: -$2500
**Penalty for Underestimating Risk**: -$3000

## Enforcement Mechanisms

### 1. Pre-Action Validation
```yaml
validation_rules:
  major_decision:
    requires: [decision_analysis]
    minimum_confidence: 75
    
  bug_fix:
    requires: [problem_analysis]
    root_cause_mandatory: true
    
  new_feature:
    requires: [decision_analysis, risk_analysis]
    architecture_review: required
    
  refactoring:
    requires: [quality_analysis, architecture_analysis]
    improvement_threshold: 20%
```

### 2. Automatic Prompting
When analysis is missing:
```
BLOCKED: <action> requires <analysis_tag>

Missing required sections:
- [ ] context
- [ ] evidence  
- [ ] recommendation

Please complete analysis before proceeding.
```

### 3. Quality Scoring
```python
def score_analysis(analysis):
    scores = {
        'evidence_based': check_evidence_links(analysis) * 0.4,
        'completeness': check_all_sections(analysis) * 0.3,
        'clarity': check_language_clarity(analysis) * 0.2,
        'actionability': check_next_steps(analysis) * 0.1
    }
    
    total = sum(scores.values())
    
    if total < 85:
        raise AnalysisQualityError(f"Score {total}% below minimum 85%")
    
    return total
```

### 4. Historical Tracking
```yaml
analysis_history:
  - id: "DEC-2024-001"
    type: "decision_analysis"
    score: 92
    outcome: "successful"
    learnings: "POC validation crucial"
    
  - id: "PROB-2024-047"
    type: "problem_analysis"
    score: 88
    outcome: "root cause found"
    learnings: "5 Whys effective for service issues"
```

## Analysis Templates

### Quick Decision Template
```xml
<decision_analysis>
  <context>Choosing between logging frameworks for new service</context>
  <options>
    <option name="Winston">
      <pros>Widely used, great ecosystem</pros>
      <cons>Configuration complexity</cons>
    </option>
    <option name="Pino">
      <pros>Fastest performance, JSON native</pros>
      <cons>Smaller ecosystem</cons>
    </option>
    <option name="Bunyan">
      <pros>Structured logging pioneer</pros>
      <cons>Less maintained</cons>
    </option>
  </options>
  <evidence>
    <benchmarks>Pino 5x faster than Winston</benchmarks>
    <research>GitHub stars: Winston 20k, Pino 6k</research>
  </evidence>
  <risks>
    <risk severity="low">
      <description>Pino ecosystem gaps</description>
      <mitigation>Write custom transports as needed</mitigation>
    </risk>
  </risks>
  <recommendation>
    <choice>Pino</choice>
    <rationale>Performance critical for high-volume service</rationale>
  </recommendation>
  <confidence>
    <level>85%</level>
    <factors>Clear benchmarks, active maintenance</factors>
  </confidence>
</decision_analysis>
```

### Emergency Problem Template
```xml
<problem_analysis>
  <problem_statement>Production API returning 500 errors</problem_statement>
  <symptoms>
    <symptom frequency="always">
      <description>500 error on /api/users endpoint</description>
      <evidence>Error logs show "Connection timeout"</evidence>
    </symptom>
  </symptoms>
  <root_cause>
    <analysis_method>Log analysis + system metrics</analysis_method>
    <findings>Database connection pool exhausted</findings>
    <verification>Pool size 10, active connections 10</verification>
  </root_cause>
  <impact>
    <users_affected>All users (100%)</users_affected>
    <urgency>critical</urgency>
  </impact>
  <solution_options>
    <option priority="1">
      <approach>Increase connection pool to 50</approach>
      <effort>5 minutes</effort>
    </option>
    <option priority="2">
      <approach>Add connection pooling monitoring</approach>
      <effort>2 hours</effort>
    </option>
  </solution_options>
</problem_analysis>
```

## Progressive Complexity Levels

### Level 1: Basic (Junior Teams)
- Simplified tag structure
- Guided prompts for each section
- Examples provided inline
- Minimum 2 options instead of 3

### Level 2: Standard (Most Teams)
- Full tag structure as shown above
- Quality scoring enforced
- Historical tracking enabled
- Peer review required

### Level 3: Advanced (Senior Teams)
- Additional sections for edge cases
- Cross-functional impact analysis
- Integration with architecture decision records
- Automated quality gates

### Level 4: Expert (Architecture Teams)
- Mathematical proofs for critical decisions
- Formal verification requirements
- Multi-stage analysis with checkpoints
- Board presentation templates

## Integration Points

### With Personas
- **Analyst**: Uses problem_analysis for research
- **Architect**: Uses architecture_analysis for all designs
- **PM**: Uses decision_analysis for feature decisions
- **Dev**: Uses quality_analysis for code reviews
- **Quality Enforcer**: Validates all analysis tags

### With Memory System
- Store all analyses with outcomes
- Surface similar past analyses
- Learn from successful patterns
- Warn about failed approaches

### With Quality Gates
- Analysis required before gate passage
- Quality score affects gate status
- Missing analysis = automatic failure
- Historical analysis affects confidence

## Success Metrics

### Quantitative
- 100% of major decisions have analysis tags
- Average analysis quality score >85%
- 50% reduction in decision reversals
- 75% faster root cause identification

### Qualitative
- Clear decision rationale for all changes
- Improved team confidence in decisions
- Better risk anticipation and mitigation
- Knowledge preservation across projects

## Common Pitfalls to Avoid

1. **Analysis Paralysis**
   - Don't over-analyze minor decisions
   - Set time boxes for analysis
   - Use templates for speed

2. **Superficial Compliance**
   - Ensure meaningful content, not just filled sections
   - Quality scoring prevents gaming
   - Random audits maintain standards

3. **Copy-Paste Analysis**
   - Each situation is unique
   - Reference past analyses but don't copy
   - Evolve templates based on learnings

4. **Ignoring Analysis Results**
   - Analysis must drive action
   - Track whether recommendations followed
   - Review outcomes against predictions

Remember: Structured thinking is not bureaucracy—it's a tool for better, faster, more confident decisions.