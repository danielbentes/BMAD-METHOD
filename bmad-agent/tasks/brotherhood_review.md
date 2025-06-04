# Brotherhood Review Task

## CRITICAL SAFETY RULES ⚠️

**MANDATORY COMPLIANCE - NO EXCEPTIONS**

1. **Honesty Requirement**: ABSOLUTELY PROHIBITED:
   - Sycophantic "looks good" responses
   - Approval without thorough testing
   - Hiding or downplaying issues
   - Agreeing to avoid conflict

2. **Evidence Mandate**: EVERY assessment MUST have:
   - Specific code/artifact references
   - Actual test execution results
   - Measurable quality metrics
   - Clear pass/fail criteria

3. **Review Gates**: MANDATORY activities:
   - 30 minutes minimum independent analysis
   - Actual functionality testing required
   - Production scenario validation
   - Written findings before discussion

4. **AI Safety Rules**:
   - NEVER approve without testing
   - ALWAYS document negative findings
   - PROHIBIT rubber-stamp reviews
   - REQUIRE specific improvement actions

5. **Rejection Triggers**: MUST REJECT if:
   - Core functionality doesn't work
   - Quality standards violated
   - Security vulnerabilities found
   - Production readiness lacking

## Purpose
Conduct honest, rigorous peer review to ensure quality and eliminate sycophantic behavior. Store review records at `.ai/quality/reviews/brotherhood-review-{date}.md`.

## Progressive Review Phases

### Phase 1: Preparation (0-20%) 📝
**Goal**: Ready for thorough review

**Entry Criteria**:
- Work claimed complete
- All artifacts available
- Test environment ready
- Time allocated (60+ min)

**Activities**:
1. Gather all deliverables
2. Set up test environment
3. Review quality gates
4. Prepare review workspace

**Exit Criteria**:
- All materials collected
- Tests ready to run
- Review template open
- 20% checkpoint passed

### Phase 2: Independent Analysis (20-60%) 🔍
**Goal**: Thorough unbiased assessment

**Entry Criteria**:
- Phase 1 complete
- No communication with reviewee
- Fresh perspective maintained

**Activities**:
1. Code/artifact inspection
2. Functionality testing
3. Quality standard checks
4. Document all findings

**Exit Criteria**:
- All tests executed
- Findings documented
- Issues categorized
- 60% checkpoint passed

### Phase 3: Collaborative Review (60-80%) 🤝
**Goal**: Discuss findings openly

**Entry Criteria**:
- Independent analysis complete
- Findings documented
- Both parties available

**Activities**:
1. Present findings honestly
2. Discuss disagreements
3. Identify root causes
4. Agree on assessment

**Exit Criteria**:
- Consensus reached
- Actions identified
- Decision made
- 80% checkpoint passed

### Phase 4: Documentation (80-100%) 📝
**Goal**: Record review outcomes

**Entry Criteria**:
- Review complete
- Decision finalized
- Actions defined

**Activities**:
1. Complete review record
2. File in quality folder
3. Update metrics
4. Share learnings

**Exit Criteria**:
- Record filed
- Team notified
- Metrics updated
- 100% complete

## Review Protocol

### Pre-Review Requirements
- [ ] Self-assessment completed honestly
- [ ] All quality gates passed
- [ ] UDTM documentation provided
- [ ] Real implementation verified (no mocks/stubs)

### Review Dimensions

#### 1. Technical Review
- [ ] **Code Quality**: Clean, maintainable, follows standards
- [ ] **Architecture**: Consistent with existing patterns
- [ ] **Performance**: Meets requirements, no obvious bottlenecks
- [ ] **Security**: No vulnerabilities, proper error handling

#### 2. Logic Review
- [ ] **Solution Appropriateness**: Best approach for the problem
- [ ] **Requirement Alignment**: Meets all specified requirements
- [ ] **Edge Case Handling**: Proper boundary condition management
- [ ] **Integration**: Works properly with existing systems

#### 3. Reality Check (CRITICAL)
- [ ] **Actually Works**: Functionality verified through testing
- [ ] **No Shortcuts**: Real implementation, not workarounds
- [ ] **Production Ready**: Would survive in production environment
- [ ] **Error Scenarios**: Handles failures gracefully

#### 4. Quality Standards
- [ ] **Zero Violations**: No Ruff or MyPy errors
- [ ] **Test Coverage**: Adequate and meaningful tests
- [ ] **Documentation**: Clear, accurate, complete
- [ ] **Maintainability**: Future developers can understand/modify

### Honest Assessment Questions
1. **Does this actually work as claimed?**
2. **Are there any shortcuts or workarounds?**
3. **Would this break in production?**
4. **Is this the best solution to the problem?**
5. **Am I being completely honest about the quality?**

### Review Process

#### Step 1: Independent Analysis (30 minutes)
- Review all artifacts without discussion
- Complete technical analysis independently
- Document initial findings and concerns
- Prepare specific questions and feedback

#### Step 2: Collaborative Discussion (15 minutes)
- Share findings openly and honestly
- Challenge assumptions and approaches
- Identify gaps and improvement opportunities
- Reach consensus on quality assessment

#### Step 3: Action Planning (15 minutes)
- Define specific improvement actions
- Assign ownership and timelines
- Establish re-review criteria if needed
- Document decisions and rationale

### Review Outcomes
- **APPROVE**: All criteria met, no issues identified
- **CONDITIONAL**: Minor fixes required, re-review needed within 24 hours
- **REJECT**: Major issues, return to planning/implementation phase

### Brotherhood Principles
- **Honesty First**: Truth over politeness
- **Quality Focus**: Excellence over speed
- **Mutual Support**: Help improve, don't just critique
- **Root Cause**: Address underlying issues, not symptoms
- **Continuous Improvement**: Learn from every review

## Anti-Sycophantic Enforcement

### Forbidden Responses
- "Looks good" without specific analysis
- "Great work" without identifying actual strengths
- "Minor issues" when major problems exist
- Agreement without independent verification

### Required Evidence
- Specific examples of quality or issues
- Reference to standards and best practices
- Demonstration of actual functionality testing
- Clear reasoning for all assessments

## Review Documentation

### Review Record Template
Save the review record at `.ai/quality/reviews/brotherhood-review-{date}.md`:

```markdown
## Brotherhood Review: [Task/Story Name]
**Date**: [YYYY-MM-DD]
**Reviewer**: [Name]
**Reviewee**: [Name]

### Technical Assessment
- **Code Quality**: [Specific findings]
- **Architecture**: [Specific findings]
- **Performance**: [Specific findings]
- **Security**: [Specific findings]

### Reality Check Results
- **Functionality Test**: [Pass/Fail with evidence]
- **Production Readiness**: [Assessment with reasoning]
- **Error Handling**: [Specific scenarios tested]

### Honest Assessment
- **Strengths**: [Specific examples]
- **Weaknesses**: [Specific issues with impact]
- **Recommendations**: [Actionable improvements]

### Final Decision
- **Outcome**: [Approve/Conditional/Reject]
- **Confidence**: [1-10 with reasoning]
- **Next Steps**: [Specific actions required]
```

## Success Criteria
- Honest evaluation with documented findings
- Specific recommendations for improvement
- Confidence in production readiness
- Team knowledge sharing achieved
- Quality standards maintained or improved

## Integration with BMAD Workflow
- **Required for**: All story completion, architecture decisions, deployment
- **Frequency**: At minimum before story done, optionally mid-implementation
- **Documentation**: All reviews tracked in project quality metrics at `.ai/quality/reviews/`
- **Learning**: Review insights feed back into process improvement
- **Storage**: Each review record saved as `.ai/quality/reviews/brotherhood-review-{date}.md`

## Error Recovery Procedures

### Common Failure Scenarios

1. **Sycophantic Behavior Detected**
   - **Detection**: Vague approval without specifics
   - **Recovery**: Restart with specific checklist
   - **Prevention**: Use evidence requirements

2. **Rushed Review**
   - **Detection**: <30 minutes spent
   - **Recovery**: Schedule proper review time
   - **Prevention**: Block calendar in advance

3. **Missing Test Evidence**
   - **Detection**: No test results documented
   - **Recovery**: Execute tests before proceeding
   - **Prevention**: Test environment ready first

4. **Conflict Avoidance**
   - **Detection**: Issues downplayed or hidden
   - **Recovery**: Anonymous issue reporting
   - **Prevention**: Emphasize honesty principle

### Recovery Protocol
1. **Recognize** the compromised review
2. **Reset** to proper review process
3. **Execute** with full rigor
4. **Document** what went wrong
5. **Learn** from the failure
6. **Prevent** future occurrences

## Success Metrics

### Quantitative Metrics
- **Issue Discovery Rate**: >2 issues per review average
- **Rejection Rate**: 15-25% (healthy skepticism)
- **Review Duration**: >60 minutes average
- **Action Item Generation**: >3 improvements per review

### Qualitative Metrics
- **Honesty**: Direct feedback without softening
- **Specificity**: Concrete examples in all feedback
- **Actionability**: Clear improvement paths
- **Learning**: New insights gained

### Early Warning Indicators
- All reviews passing without issues
- Reviews completing too quickly
- Vague or generic feedback
- No difficult conversations

## Continuous Improvement

### Post-Review Analysis
1. **Review Effectiveness**:
   - Did we catch real issues?
   - Was feedback actionable?
   - Did quality improve?

2. **Pattern Recognition**:
   - Common quality issues
   - Frequent blind spots
   - Successful practices

3. **Process Enhancement**:
   - Refine review checklists
   - Improve testing approaches
   - Enhance documentation

### Knowledge Capture
- Archive significant findings
- Build review best practices
- Document quality patterns
- Share team learnings

### Cultural Reinforcement
- Celebrate honest feedback
- Reward issue discovery
- Support improvement efforts
- Model brotherhood principles