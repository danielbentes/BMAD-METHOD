# Ultra-Deep Thinking Mode (UDTM) Task

## CRITICAL SAFETY RULES ⚠️

**MANDATORY COMPLIANCE - NO EXCEPTIONS**

1. **Time Investment Rule**: NEVER shortcut phases:
   - Phase 1: MINIMUM 30 minutes multi-angle analysis
   - Phase 2: MINIMUM 15 minutes assumption challenge
   - Phase 3: MINIMUM 20 minutes triple verification
   - Phase 4: MINIMUM 15 minutes weakness hunting
   - Phase 5: MINIMUM 10 minutes final reflection
   - Total: MINIMUM 90 minutes for complete UDTM

2. **Evidence Requirements**: EVERY conclusion MUST have:
   - Documented evidence from multiple sources
   - Specific examples or test cases
   - Quantifiable metrics where possible
   - Clear reasoning chain documented

3. **Confidence Threshold**: MANDATORY requirements:
   - MUST achieve >95% confidence to proceed
   - MUST document all uncertainties
   - MUST identify mitigation for each risk
   - MUST get peer validation for critical decisions

4. **AI Safety Rules**:
   - NEVER skip any analysis phase
   - ALWAYS document negative findings
   - PROHIBIT proceeding with <95% confidence
   - REQUIRE external validation for assumptions

5. **Abort Conditions**: MUST STOP if:
   - Cannot achieve 95% confidence
   - Critical assumptions cannot be validated
   - Multiple high-risk issues identified
   - Time constraints prevent full analysis

## Purpose
Execute rigorous analysis and verification protocol to ensure highest quality decision-making and implementation. Store UDTM analysis results at `.ai/quality/validations/udtm-analysis-{task}-{date}.md`.

## Progressive Deep-Thinking Phases

### Pre-Flight Check (0-5%) 🚫
**Goal**: Ensure readiness for deep analysis

**Entry Criteria**:
- Clear problem/decision defined
- All relevant documentation available
- 90+ minutes allocated
- Distraction-free environment

**Activities**:
1. Define scope of analysis
2. Gather all source materials
3. Set up analysis workspace
4. Clear mental state

**Exit Criteria**:
- Scope crystal clear
- Materials organized
- Timer set for phases
- Ready for deep work

## Protocol

### Phase 1: Multi-Angle Analysis (30 minutes minimum) - Progress: 5-35% 🔍
- [ ] **Technical Perspective**: Correctness, performance, maintainability
- [ ] **Business Logic Perspective**: Alignment with requirements
- [ ] **Integration Perspective**: Compatibility with existing systems
- [ ] **Edge Case Perspective**: Boundary conditions and failure modes
- [ ] **Security Perspective**: Vulnerabilities and attack vectors
- [ ] **Performance Perspective**: Resource usage and scalability

### Phase 2: Assumption Challenge (15 minutes) - Progress: 35-50% 🤔
1. **List all assumptions** made during analysis
2. **Challenge each assumption** - attempt to disprove
3. **Document evidence** for/against each assumption
4. **Identify critical dependencies** on assumptions

### Phase 3: Triple Verification (20 minutes) - Progress: 50-70% ✅
- [ ] **Source 1**: Official documentation/specifications
- [ ] **Source 2**: Existing codebase patterns and standards
- [ ] **Source 3**: External validation (tests, tools, references)
- [ ] **Cross-reference**: Ensure all three sources align

### Phase 4: Weakness Hunting (15 minutes) - Progress: 70-85% 🎯
- [ ] What could break this solution?
- [ ] What edge cases might we have missed?
- [ ] What are the failure modes?
- [ ] What assumptions are we making that could be wrong?
- [ ] What integration points could fail?

### Phase 5: Final Reflection (10 minutes) - Progress: 85-100% 🏁
- [ ] Re-examine entire reasoning chain from scratch
- [ ] Document confidence level (must be >95% to proceed)
- [ ] Identify any remaining uncertainties
- [ ] Confirm all quality gates can be met

## Output Requirements
Document all phases with specific findings, evidence, and confidence assessments. Save the complete UDTM analysis at `.ai/quality/validations/udtm-analysis-{task}-{date}.md`.

## Success Criteria
- All phases completed with documented evidence
- Confidence level >95%
- All assumptions validated or flagged as risks
- Quality gates confirmed achievable

## Usage Instructions
1. Execute this task before any major implementation or decision
2. Document all findings in the UDTM Analysis Template at `.ai/quality/validations/udtm-analysis-{task}-{date}.md`
3. Do not proceed without achieving >95% confidence
4. Share analysis with team for brotherhood review
5. Store completed analysis for future reference and learning

## Integration with BMAD Workflow
- **BREAK Phase**: Use UDTM for problem decomposition
- **MAKE Phase**: Apply before each implementation sprint
- **ANALYZE Phase**: Execute for issue investigation
- **DELIVER Phase**: Final validation before deployment
- **Documentation**: All UDTM analyses stored at `.ai/quality/validations/` for tracking and learning
- **Quality Metrics**: UDTM completion tracked in project quality metrics

## Error Recovery Procedures

### Common Failure Scenarios

1. **Low Confidence Result (<95%)**
   - **Detection**: Final confidence below threshold
   - **Recovery**: Identify specific gaps, gather more data
   - **Prevention**: More thorough initial analysis

2. **Time Pressure Shortcuts**
   - **Detection**: Phases completed too quickly
   - **Recovery**: Reset and allocate proper time
   - **Prevention**: Block calendar for full 90 minutes

3. **Assumption Validation Failure**
   - **Detection**: Core assumptions proven false
   - **Recovery**: Rebuild analysis with new facts
   - **Prevention**: Challenge assumptions early

4. **Conflicting Evidence**
   - **Detection**: Sources disagree significantly
   - **Recovery**: Seek authoritative resolution
   - **Prevention**: Use primary sources

### Recovery Protocol
1. **Pause** the analysis
2. **Identify** the specific issue
3. **Document** what went wrong
4. **Determine** if continuation is viable
5. **Either** fix and continue OR abort with clear reasoning
6. **Learn** from the failure for next time

## Success Metrics

### Quantitative Metrics
- **Completion Rate**: >90% of UDTMs reach 95% confidence
- **Time Investment**: Average 90-120 minutes per UDTM
- **Issue Discovery**: >3 significant findings per UDTM
- **Decision Quality**: <5% decisions need reversal

### Qualitative Metrics
- **Depth**: Analysis uncovers non-obvious insights
- **Clarity**: Reasoning chain easily followed
- **Evidence**: Strong support for conclusions
- **Actionability**: Clear next steps identified

### Early Warning Indicators
- Rushing through phases
- Difficulty finding evidence
- Many unvalidated assumptions
- Confidence hovering at threshold

## Continuous Improvement

### Post-UDTM Review
1. **Effectiveness Assessment**:
   - Did analysis prevent issues?
   - Were findings accurate?
   - Was time well spent?

2. **Pattern Recognition**:
   - Common assumption failures
   - Frequent weakness types
   - Successful analysis techniques

3. **Process Enhancement**:
   - Refine phase durations
   - Improve evidence sources
   - Enhance documentation templates

### Knowledge Capture
- Archive all UDTM analyses
- Extract reusable insights
- Build assumption libraries
- Document decision patterns

### Team Learning
- Share UDTM findings in reviews
- Discuss challenging analyses
- Celebrate prevented issues
- Build collective wisdom