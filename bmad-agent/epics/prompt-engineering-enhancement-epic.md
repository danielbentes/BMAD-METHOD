# Epic: Advanced Prompt Engineering Implementation for BMAD Method

## Epic Overview

**Epic Goal:** Transform all BMAD Method prompts, tasks, workflows, and instructions using enterprise-grade prompt engineering principles to achieve:
- 95% first-attempt success rate for persona activations
- 80% reduction in clarification requests
- Zero critical anti-pattern violations
- Enhanced safety through prompt-based enforcement

**Research Foundation:** Based on comprehensive analysis of enterprise prompt engineering patterns, including Anthropic's Constitutional AI, OpenAI's safety frameworks, and proven production patterns from major tech companies.

## Implementation Principles

### Core Enhancement Framework
1. **5-Component Structure:** System Role + Task Spec + Context + Examples + Output Format
2. **Safety-First Language:** Prohibitive constraints with penalty structures
3. **Progressive Disclosure:** Phased information release with validation gates
4. **Evidence-Based Decisions:** Mandatory data backing for all choices
5. **Memory Intelligence:** Pattern recognition and proactive guidance

## Story Breakdown

### Story 1: Enhance Core Persona Files with 5-Component Structure

**As a** BMAD user  
**I want** all persona files to follow the proven 5-component prompt structure  
**So that** persona activations are more reliable and effective

**Scope:**
- Transform all 10 persona files in `bmad-agent/personas/`
- Implement standardized structure across all personas
- Add safety constraints and validation requirements

**Acceptance Criteria:**

1. **System Role Enhancement (Component 1):**
   ```markdown
   # CRITICAL ROLE: [PERSONA TITLE]
   
   ## YOU ARE THE [ROLE] AND YOU MUST:
   - **NEVER** [list critical prohibitions]
   - **ALWAYS** [list mandatory behaviors]
   - **MUST** [list non-negotiable requirements]
   
   ## FAILURE CONSEQUENCES:
   - Quality violations result in IMMEDIATE task termination
   - Anti-patterns trigger MANDATORY escalation
   - Assumption-based decisions VOID all outputs
   ```

2. **Task Specification (Component 2):**
   ```markdown
   ## PRIMARY RESPONSIBILITIES (IN PRIORITY ORDER):
   1. [First priority with success criteria]
   2. [Second priority with measurable outcomes]
   3. [Third priority with validation requirements]
   
   ## AVAILABLE COMMANDS:
   - `/command1` - [Description with expected outcome]
   - `/command2` - [Description with validation steps]
   
   ## SUCCESS METRICS:
   - [ ] Metric 1: [Quantifiable target]
   - [ ] Metric 2: [Measurable outcome]
   - [ ] Metric 3: [Verifiable result]
   ```

3. **Context Integration (Component 3):**
   ```markdown
   ## BEFORE STARTING ANY TASK:
   1. **Memory Search**: Query for similar past experiences
   2. **Context Verification**: Validate all prerequisites
   3. **Integration Check**: Confirm handoff requirements
   
   ## INTEGRATION POINTS:
   - **Receives From**: [Personas] with [artifacts]
   - **Hands Off To**: [Personas] with [deliverables]
   - **Collaborates With**: [Personas] for [purposes]
   ```

4. **Few-Shot Examples (Component 4):**
   ```markdown
   ## EXAMPLE INTERACTIONS:
   
   ### Example 1: [Common Scenario]
   **Input**: [User request]
   **Process**: [Step-by-step approach]
   **Output**: [Expected result format]
   
   ### Anti-Pattern Example: [What NOT to do]
   **Wrong Approach**: [Common mistake]
   **Why It Fails**: [Specific reason]
   **Correct Approach**: [Proper method]
   ```

5. **Output Format (Component 5):**
   ```markdown
   ## REQUIRED OUTPUT FORMAT:
   
   ### Response Structure:
   ```
   [PERSONA_NAME] Analysis:
   
   ## Executive Summary
   [2-3 sentence overview]
   
   ## Detailed Findings
   1. [Finding with evidence]
   2. [Finding with data backing]
   
   ## Recommendations
   - [ ] Action 1: [Specific step]
   - [ ] Action 2: [Measurable outcome]
   
   ## Quality Validation
   ✓ All gates passed
   ✓ No anti-patterns detected
   ✓ Evidence documented
   ```
   ```

**Implementation Files:**
- `analyst.md` - Research and analysis expert
- `architect.md` - System design authority
- `bmad.md` - Base orchestrator
- `design-architect.md` - UI/UX specialist
- `dev.ide.md` - Development implementation
- `pm.md` - Product strategy
- `po.md` - Process governance
- `quality_enforcer.md` - Quality assurance
- `sm.ide.md` - Agile facilitation (IDE)
- `sm.md` - Agile facilitation (base)

### Story 2: Implement Safety-First Quality Enforcement

**As a** quality enforcer  
**I want** all quality tasks to use enterprise-grade safety language  
**So that** quality violations are prevented rather than detected

**Scope:**
- Transform all quality task files in `bmad-agent/quality-tasks/`
- Implement prohibitive constraints with penalties
- Add progressive validation gates

**Acceptance Criteria:**

1. **Critical Safety Rules Section:**
   ```markdown
   ## CRITICAL SAFETY RULES (MANDATORY COMPLIANCE)
   
   ### RULE 0: WORK STOPPAGE PROTOCOL
   If ANY quality gate fails, you MUST:
   1. **STOP** all work immediately
   2. **DOCUMENT** exact failure point
   3. **ESCALATE** to Quality Enforcer
   4. **WAIT** for remediation approval
   
   **PENALTY**: Proceeding past failed gates = -$1000 penalty + process review
   
   ### RULE 1: ANTI-PATTERN DETECTION
   **NEVER PROCEED** if these patterns detected:
   - Mock services in production paths
   - Placeholder code (TODO, FIXME, NotImplemented)
   - Assumption-based implementations
   - Generic exception handling
   - Untested critical paths
   
   ### RULE 2: EVIDENCE REQUIREMENT
   **ALL** decisions require:
   - Quantitative data backing
   - Expert validation
   - Historical precedent
   - Risk assessment
   ```

2. **Progressive Quality Gates:**
   ```markdown
   ## QUALITY GATE PROGRESSION
   
   ### Gate 1: Initialization (25%)
   - [ ] All inputs validated
   - [ ] Prerequisites confirmed
   - [ ] Success criteria defined
   **GATE 1 CHECKPOINT**: Cannot proceed without 100% completion
   
   ### Gate 2: Implementation (50%)
   - [ ] Core logic validated
   - [ ] Anti-patterns checked
   - [ ] Performance verified
   **GATE 2 CHECKPOINT**: Mandatory peer review required
   
   ### Gate 3: Integration (75%)
   - [ ] End-to-end testing complete
   - [ ] Edge cases handled
   - [ ] Security validated
   **GATE 3 CHECKPOINT**: Architecture approval required
   
   ### Gate 4: Delivery (100%)
   - [ ] All documentation complete
   - [ ] Deployment verified
   - [ ] Monitoring enabled
   **GATE 4 CHECKPOINT**: Quality Enforcer sign-off mandatory
   ```

3. **Enforcement Mechanisms:**
   ```markdown
   ## ENFORCEMENT PROTOCOLS
   
   ### Violation Detection:
   - **Automated Scanning**: Every 5 minutes during development
   - **Manual Review**: At each gate checkpoint
   - **Peer Validation**: Before any handoff
   
   ### Violation Response:
   1. **Minor** (style, naming): Log + Fix suggestion
   2. **Major** (logic, performance): Stop + Review required
   3. **Critical** (security, data): Halt + Escalation mandatory
   
   ### Recovery Requirements:
   - Root cause analysis document
   - Remediation plan with timeline
   - Prevention strategy update
   - Team training if pattern repeated
   ```

**Implementation Files:**
- `ultra-deep-thinking-mode.md`
- `architecture-udtm-analysis.md`
- `requirements-udtm-analysis.md`
- `technical-decision-validation.md`
- `technical-standards-enforcement.md`
- `test-coverage-requirements.md`
- `story-quality-validation.md`
- `quality-metrics-tracking.md`
- `evidence-requirements-prioritization.md`
- `code-review-standards.md`

### Story 3: Enhance Task Files with Progressive Disclosure

**As a** BMAD user executing tasks  
**I want** all task files to use progressive disclosure with validation  
**So that** task execution is reliable and self-correcting

**Scope:**
- Transform all task files in `bmad-agent/tasks/`
- Implement phased execution with checkpoints
- Add validation and error recovery

**Acceptance Criteria:**

1. **Phase-Based Structure:**
   ```markdown
   ## TASK EXECUTION PHASES
   
   ### PHASE 1: Pre-Execution Validation
   **MANDATORY BEFORE PROCEEDING:**
   - [ ] User intent confirmed and documented
   - [ ] All inputs verified and accessible
   - [ ] Success criteria agreed upon
   - [ ] Quality gates scheduled
   - [ ] Resource availability confirmed
   
   **PHASE 1 GATE**: Do NOT proceed until ALL items checked
   
   ### PHASE 2: Core Execution
   **SYSTEMATIC PROGRESSION:**
   Step 2.1: [Action with validation]
   - Expected outcome: [Specific result]
   - Validation: [How to verify]
   - Error handling: [Recovery steps]
   
   Step 2.2: [Next action]
   [Continue pattern...]
   
   **PHASE 2 GATE**: Quality checkpoint required
   
   ### PHASE 3: Validation & Handoff
   **COMPLETION REQUIREMENTS:**
   - [ ] All outputs validated against criteria
   - [ ] No anti-patterns in deliverables
   - [ ] Documentation complete
   - [ ] Next persona briefed
   - [ ] Memory updated with outcomes
   
   **PHASE 3 GATE**: Sign-off before completion
   ```

2. **Validation Checkpoints:**
   ```markdown
   ## VALIDATION FRAMEWORK
   
   ### After Each Major Step:
   ```python
   validation_checklist = {
       "output_quality": "Meets defined criteria",
       "anti_patterns": "None detected",
       "user_feedback": "Incorporated",
       "quality_gates": "Passed",
       "documentation": "Updated"
   }
   ```
   
   ### Checkpoint Failure Protocol:
   1. **STOP** current execution
   2. **ANALYZE** failure reason
   3. **PROPOSE** corrective action
   4. **CONFIRM** with user
   5. **RETRY** from safe point
   ```

3. **Error Prevention Framework:**
   ```markdown
   ## ERROR PREVENTION MATRIX
   
   ### Common Failure Patterns:
   | Pattern | Prevention | Detection | Recovery |
   |---------|------------|-----------|----------|
   | Missing context | Mandatory prereq check | Validation gate | Context restoration |
   | Invalid input | Type validation | Input sanitization | User clarification |
   | Resource unavailable | Availability check | Timeout handling | Alternative approach |
   | Quality violation | Continuous monitoring | Gate checkpoint | Rollback & fix |
   ```

**Implementation Files:**
- Core creation tasks (PRD, architecture, frontend, stories)
- Utility tasks (doc-sharding, checklist-run, core-dump)
- Intelligence tasks (research prompts, AI prompts)
- Recovery tasks (correct-course, error handling)

### Story 4: Upgrade Orchestrator with Enterprise Command Structure

**As a** BMAD orchestrator user  
**I want** enhanced command structure with safety protocols  
**So that** orchestration is reliable and error-resistant

**Scope:**
- Enhance orchestrator files with command safety
- Implement progressive command disclosure
- Add memory safety protocols

**Acceptance Criteria:**

1. **Command Safety Protocols:**
   ```markdown
   ## COMMAND EXECUTION SAFETY
   
   ### Pre-Execution Validation:
   - [ ] Command exists in registry
   - [ ] User has appropriate context
   - [ ] Parameters validated
   - [ ] No conflicts detected
   - [ ] Resources available
   
   ### Execution Monitoring:
   - Real-time progress tracking
   - Anomaly detection
   - Resource usage monitoring
   - Quality gate enforcement
   - Error interception
   
   ### Post-Execution Verification:
   - Output validation
   - Side effect check
   - Memory update
   - Success metrics
   - User satisfaction
   ```

2. **Progressive Command Disclosure:**
   ```markdown
   ## COMMAND AVAILABILITY FRAMEWORK
   
   ### Level 1: Essential Commands (Always Available)
   Commands for basic operation and help:
   - `/help` - Contextual assistance
   - `/status` - System state
   - `/agents` - Persona directory
   
   ### Level 2: Persona Commands (Context-Aware)
   Activated based on current needs:
   - Product commands when planning
   - Technical commands when building
   - Quality commands when validating
   
   ### Level 3: Advanced Commands (Expert Mode)
   Requires explicit activation:
   - `/udtm` - Deep analysis protocols
   - `/consult` - Multi-persona panels
   - `/override` - Safety bypasses (logged)
   ```

3. **Memory Safety Implementation:**
   ```markdown
   ## MEMORY OPERATION SAFETY
   
   ### Privacy Protection:
   - **NEVER** store passwords or keys
   - **ALWAYS** anonymize personal data
   - **MUST** respect consent preferences
   
   ### Data Integrity:
   - Validate before storage
   - Encrypt sensitive info
   - Version all changes
   - Maintain audit trail
   
   ### Access Control:
   - User-owned data only
   - Project-scoped access
   - Time-based expiration
   - Explicit permissions
   ```

**Implementation Files:**
- `ide-bmad-orchestrator.md`
- `ide-bmad-orchestrator.cfg.md`
- `web-bmad-orchestrator-agent.md`
- `web-bmad-orchestrator-agent.cfg.md`
- `commands/command-registry.yml`

### Story 5: Implement Evidence-Based Templates

**As a** BMAD user creating artifacts  
**I want** all templates to require evidence and validation  
**So that** outputs are high-quality and defensible

**Scope:**
- Enhance all template files with evidence requirements
- Add built-in validation checkboxes
- Implement quality assurance sections

**Acceptance Criteria:**

1. **Evidence Requirements:**
   ```markdown
   ## EVIDENCE REQUIREMENTS
   
   ### For Each Claim/Decision:
   - [ ] **Primary Source**: Direct evidence link
   - [ ] **Data Backing**: Quantitative support
   - [ ] **Expert Validation**: SME review
   - [ ] **User Validation**: Stakeholder confirmation
   
   ### Evidence Quality Matrix:
   | Type | Required | Preferred | Optimal |
   |------|----------|-----------|---------|
   | Age | < 1 year | < 6 months | < 3 months |
   | Source | Published | Peer-reviewed | Meta-analysis |
   | Confidence | 70% | 85% | 95% |
   ```

2. **Validation Framework:**
   ```markdown
   ## TEMPLATE COMPLETION CHECKLIST
   
   ### Content Validation:
   - [ ] No placeholders remaining
   - [ ] All sections complete
   - [ ] Links functional
   - [ ] Data current
   - [ ] Formatting consistent
   
   ### Technical Validation:
   - [ ] Feasibility confirmed
   - [ ] Resources realistic
   - [ ] Timeline achievable
   - [ ] Risks identified
   - [ ] Mitigations planned
   
   ### Quality Validation:
   - [ ] Peer reviewed
   - [ ] Expert approved
   - [ ] User accepted
   - [ ] Metrics defined
   - [ ] Success measurable
   ```

**Implementation Files:**
- `templates/prd-tmpl.md`
- `templates/architecture-tmpl.md`
- `templates/front-end-architecture-tmpl.md`
- `templates/front-end-spec-tmpl.md`
- `templates/project-brief-tmpl.md`
- `templates/story-tmpl.md`

### Story 6: Enhance Memory Integration

**As a** BMAD system  
**I want** enhanced memory patterns across components  
**So that** the system learns and improves continuously

**Scope:**
- Standardize memory integration patterns
- Implement proactive intelligence
- Add pattern recognition capabilities

**Acceptance Criteria:**

1. **Standardized Memory Patterns:**
   ```markdown
   ## MEMORY INTEGRATION STANDARD
   
   ### Pre-Task Queries:
   ```python
   standard_queries = [
       f"successful {task_type} patterns",
       f"common {task_type} failures",
       f"user preferences for {task_type}",
       f"{context} optimization patterns"
   ]
   ```
   
   ### During-Task Tracking:
   - Decision points with rationale
   - Success/failure indicators
   - Performance metrics
   - User feedback
   
   ### Post-Task Storage:
   - Structured outcome data
   - Lessons learned
   - Pattern updates
   - Cross-references
   ```

2. **Proactive Intelligence:**
   ```markdown
   ## PROACTIVE GUIDANCE SYSTEM
   
   ### Pattern Detection Triggers:
   - Similar context → Surface insights
   - Risk pattern → Provide warnings
   - Success pattern → Suggest replication
   - User preference → Auto-optimize
   
   ### Intelligence Delivery:
   💡 **Insight**: Based on 5 similar cases...
   ⚠️ **Warning**: This approach failed 3/4 times...
   🎯 **Suggestion**: Pattern X succeeded 95%...
   📚 **Reference**: See PROJECT-Y for example...
   ```

**Implementation Files:**
- `memory/memory-system-architecture.md`
- `tasks/memory-operations-task.md`
- All persona files (memory sections)
- All task files (memory integration)

### Story 7: Implement Advanced Error Handling

**As a** BMAD component  
**I want** sophisticated error handling and recovery  
**So that** the system is resilient and self-healing

**Scope:**
- Create comprehensive error classification
- Implement automatic recovery protocols
- Add learning from failures

**Acceptance Criteria:**

1. **Error Classification System:**
   ```markdown
   ## ERROR TAXONOMY
   
   ### Critical (System Halt):
   - Quality gate failures
   - Anti-pattern detection
   - Security violations
   - Data corruption risk
   
   ### Warning (Proceed with Caution):
   - Performance degradation
   - Incomplete information
   - Suboptimal approach
   - Resource constraints
   
   ### Info (Log and Continue):
   - Style violations
   - Optimization opportunities
   - Documentation gaps
   - Best practice suggestions
   ```

2. **Recovery Protocols:**
   ```markdown
   ## AUTOMATIC RECOVERY FRAMEWORK
   
   ### Decision Tree:
   ```
   Error Detected
   ├─ Critical? → HALT → Escalate → Manual intervention
   ├─ Warning? → Log → Suggest fix → User decision
   └─ Info? → Log → Auto-fix if available → Continue
   ```
   
   ### Recovery Actions:
   - **State Recovery**: Restore last known good
   - **Data Recovery**: Validate and repair
   - **Process Recovery**: Restart from checkpoint
   - **Context Recovery**: Rebuild from memory
   ```

3. **Learning Integration:**
   ```markdown
   ## FAILURE LEARNING SYSTEM
   
   ### Capture Protocol:
   - Error context and state
   - Recovery attempts
   - Resolution method
   - Prevention strategy
   
   ### Pattern Analysis:
   - Frequency tracking
   - Root cause clustering
   - Impact assessment
   - Prevention effectiveness
   
   ### System Updates:
   - Validation rule updates
   - Recovery strategy improvements
   - Documentation enhancements
   - Training recommendations
   ```

**Implementation Files:**
- `error_handling/error-recovery.md`
- `error_handling/fallback-personas.md`
- Integration into all components

## Implementation Plan

### Phase 1: High Priority (Week 1)
1. Story 1: Core persona enhancements
2. Story 2: Quality enforcement implementation
3. Story 7: Error handling framework

### Phase 2: Medium Priority (Week 2)
4. Story 3: Task file enhancements
5. Story 4: Orchestrator upgrades

### Phase 3: Low Priority (Week 3)
6. Story 5: Template improvements
7. Story 6: Memory integration enhancement

## Success Metrics

### Quantitative Targets:
- **First-Attempt Success**: 95% (from 70%)
- **Clarification Requests**: -80% reduction
- **Anti-Pattern Violations**: 0 critical
- **User Satisfaction**: 90%+ positive

### Quality Indicators:
- All components follow 5-component structure
- Safety protocols active in all critical paths
- Progressive disclosure implemented throughout
- Evidence-based decision making enforced

### System Health:
- Error detection < 100ms
- Recovery success > 95%
- Memory utilization > 80%
- Pattern recognition accuracy > 85%

## Risk Mitigation

### Implementation Risks:
1. **Backward Compatibility**: Maintain fallback modes
2. **User Learning Curve**: Provide migration guides
3. **Performance Impact**: Monitor and optimize
4. **Over-Engineering**: Balance safety with usability

### Mitigation Strategies:
- Phased rollout with testing
- User feedback loops
- Performance benchmarking
- Regular retrospectives

## Conclusion

This epic transforms BMAD from a good prompt system into an enterprise-grade, self-improving, safety-first development framework. By implementing these seven stories, we achieve:

1. **Reliability**: Consistent, predictable behavior
2. **Safety**: Proactive error prevention
3. **Intelligence**: Continuous learning and improvement
4. **Quality**: Evidence-based, validated outputs
5. **Resilience**: Self-healing capabilities

The investment in prompt engineering will yield exponential returns in development velocity, quality, and user satisfaction.