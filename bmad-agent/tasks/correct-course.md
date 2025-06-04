# Correct Course Task

## CRITICAL SAFETY RULES - MANDATORY COMPLIANCE

### STOP CONDITIONS - ABORT IMMEDIATELY IF:
- Change would violate core architectural principles
- Impact analysis reveals >50% scope change to MVP
- Security vulnerabilities would be introduced
- Data loss or corruption risk identified
- User explicitly states "ignore the problem" or "skip analysis"

### MANDATORY VALIDATIONS BEFORE PROCEEDING:
1. **Change Legitimacy**: Verify change trigger is valid and documented
2. **Artifact Integrity**: Confirm all affected artifacts are accessible
3. **Impact Scope**: Preliminary assessment shows manageable impact
4. **Rollback Feasibility**: Ensure changes can be undone if needed
5. **Stakeholder Alignment**: Confirm authority to propose changes

### QUALITY GATES - MUST PASS ALL:
- [ ] Change trigger clearly documented
- [ ] All affected artifacts identified
- [ ] Impact analysis methodology agreed upon
- [ ] User consent for change analysis
- [ ] Backup of current state available

## Purpose

- Guide a structured response to a change trigger using the `change-checklist`.
- Analyze the impacts of the change on epics, project artifacts, and the MVP, guided by the checklist's structure.
- Explore potential solutions (e.g., adjust scope, rollback elements, rescope features) as prompted by the checklist.
- Draft specific, actionable proposed updates to any affected project artifacts (e.g., epics, user stories, PRD sections, architecture document sections) based on the analysis.
- Produce a consolidated "Sprint Change Proposal" document at `.ai/current/analysis/change-proposal-{date}.md` that contains the impact analysis and the clearly drafted proposed edits for user review and approval.
- Ensure a clear handoff path if the nature of the changes necessitates fundamental replanning by other core agents (like PM or Architect).

## Progressive Disclosure Phases

### Phase 1: Change Validation (MANDATORY)
1. Document change trigger and context
2. Verify artifact accessibility
3. Assess preliminary impact scope
4. Confirm user authority
5. **GATE**: Valid change request → Continue to Phase 2

### Phase 2: Impact Analysis
1. Load change-checklist
2. Analyze epic/story impacts
3. Identify artifact conflicts
4. Evaluate path options
5. **GATE**: Analysis complete → Continue to Phase 3

### Phase 3: Solution Development
1. Draft proposed changes
2. Validate technical feasibility
3. Assess risk factors
4. Create rollback plan
5. **GATE**: Solutions viable → Continue to Phase 4

### Phase 4: Proposal Finalization
1. Compile change proposal
2. Review with user
3. Incorporate feedback
4. Obtain approval
5. **FINAL GATE**: Proposal approved → Task Complete

## Instructions

### 1. Initial Setup & Mode Selection with Safety Validation

#### Pre-Execution Safety Check:
1. **Validate Change Request**
   - Document the change trigger with timestamp
   - Confirm change source is authorized
   - Check for emergency override conditions

2. **Artifact Availability Verification**
   ```python
   required_artifacts = [
       "PRD",
       "Epics/Stories", 
       "Architecture Documents",
       "UI/UX Specifications",
       "change-checklist"
   ]
   
   for artifact in required_artifacts:
       if not verify_artifact_access(artifact):
           raise ArtifactAccessError(f"Cannot access {artifact}")
   ```

3. **Impact Assessment Threshold**
   - If preliminary impact >30% of MVP scope:
     - Escalate to senior stakeholder
     - Require explicit approval to proceed

#### Mode Selection Protocol:
- **Acknowledge Task & Inputs:**
  - Confirm: "Initiating Correct Course Task for change analysis and proposal generation."
  - Display change trigger: "{change_description}"
  - Show perceived impact level: "{impact_assessment}"
  - List accessible artifacts with status indicators

- **Establish Interaction Mode:**
  ```
  Please select your preferred analysis mode:
  
  1. **Incremental Mode (Recommended for complex changes)**
     - Step-by-step checklist progression
     - Collaborative refinement at each stage
     - Higher accuracy, more time required
     - Best for: Critical changes, architectural impacts
  
  2. **Batch Mode (YOLO - for experienced users)**
     - Rapid analysis and proposal generation
     - Single comprehensive review cycle
     - Faster completion, requires careful review
     - Best for: Minor changes, clear scope
  
  Enter choice (1 or 2):
  ```

- **Mode Confirmation & Safeguards:**
  - For Batch Mode, add warning: "⚠️ Batch mode skips incremental validation. Ensure you're comfortable reviewing comprehensive changes."
  - Record mode selection in audit log
  - Set appropriate timeout limits (Incremental: 60min, Batch: 30min)

- **Process Explanation with Expectations:**
  "We'll analyze the change using the structured change-checklist. Based on your selected {mode} mode:
  - Estimated completion: {time_estimate}
  - Checkpoints: {checkpoint_count}
  - Deliverable: Sprint Change Proposal document
  - Next steps: {next_steps_preview}"

### 2. Execute Checklist Analysis with Risk Management

#### Systematic Analysis Protocol:

1. **Load and Validate Checklist**
   ```python
   checklist = load_change_checklist()
   if not validate_checklist_structure(checklist):
       use_fallback_checklist()
   ```

2. **Section-by-Section Processing**
   
   **Section 1: Change Context Analysis**
   - Severity classification: Critical/High/Medium/Low
   - Scope boundaries: Clearly define what's affected
   - Risk assessment: Security, performance, data integrity
   - Rollback complexity: Simple/Moderate/Complex
   
   **Section 2: Epic/Story Impact Analysis**
   - Direct impacts: Stories requiring modification
   - Cascade effects: Dependent stories affected
   - Timeline impacts: Sprint/milestone adjustments
   - Resource implications: Additional effort required
   
   **Section 3: Artifact Conflict Resolution**
   - Identify conflicting requirements
   - Document resolution strategies
   - Validate architectural alignment
   - Ensure consistency across artifacts
   
   **Section 4: Path Evaluation**
   - Option A: Minimal change (patch approach)
   - Option B: Refactor affected components
   - Option C: Architectural adjustment
   - Option D: Scope modification

3. **Risk Mitigation Requirements**
   For each identified risk:
   - Severity rating (1-5)
   - Mitigation strategy
   - Fallback plan
   - Success criteria

4. **Checkpoint Validations**
   - After each section in Incremental mode
   - After full analysis in Batch mode
   - Abort conditions check at each checkpoint
   - User consent before proceeding

5. **Decision Recording**
   ```markdown
   ## Decision Log
   - **Item**: {checklist_item}
   - **Status**: [x] Addressed | [ ] Pending | [!] Blocked
   - **Finding**: {analysis_result}
   - **Decision**: {agreed_action}
   - **Rationale**: {reasoning}
   - **Risk Level**: {risk_assessment}
   ```

### 3. Draft Proposed Changes with Validation

#### Change Drafting Protocol:

1. **Artifact Impact Matrix**
   ```markdown
   | Artifact | Change Type | Risk Level | Rollback Complexity |
   |----------|-------------|------------|--------------------|
   | Epic-1   | Modify      | Medium     | Simple             |
   | Story-3  | Remove      | High       | Complex            |
   | PRD §4   | Update      | Low        | Simple             |
   ```

2. **Change Templates by Type**
   
   **Story Modification Template:**
   ```markdown
   ### Story: [ID] - [Title]
   **Current State:**
   - Text: {current_text}
   - AC: {current_criteria}
   - Priority: {current_priority}
   
   **Proposed State:**
   - Text: {new_text}
   - AC: {new_criteria}
   - Priority: {new_priority}
   
   **Justification:** {why_needed}
   **Risk Assessment:** {potential_issues}
   **Dependencies:** {affected_stories}
   ```
   
   **Architecture Update Template:**
   ```markdown
   ### Component: [Name]
   **Change Type:** [Add|Modify|Remove]
   **Current Design:**
   ```mermaid
   {current_diagram}
   ```
   **Proposed Design:**
   ```mermaid
   {new_diagram}
   ```
   **Impact Analysis:** {downstream_effects}
   **Migration Path:** {how_to_implement}
   ```

3. **Validation Requirements**
   - Technical feasibility check
   - Consistency with existing patterns
   - No introduction of anti-patterns
   - Performance impact assessment
   - Security implications review

4. **User Review Process**
   - **Incremental Mode**: Review each change as drafted
   - **Batch Mode**: Present all changes in categories
   - Require explicit approval for high-risk changes
   - Document any concerns or modifications

### 4. Generate "Sprint Change Proposal" with Edits

- Synthesize the complete `change-checklist` analysis (covering findings from Sections 1-4) and all the agreed-upon proposed edits (from Instruction 3) into a single document titled "Sprint Change Proposal" saved at `.ai/current/analysis/change-proposal-{date}.md`. This proposal should align with the structure suggested by Section 5 of the `change-checklist` (Proposal Components).
- The proposal must clearly present:
  - **Analysis Summary:** A concise overview of the original issue, its analyzed impact (on epics, artifacts, MVP scope), and the rationale for the chosen path forward.
  - **Specific Proposed Edits:** For each affected artifact, clearly show or describe the exact changes (e.g., "Change Story X.Y from: [old text] To: [new text]", "Add new Acceptance Criterion to Story A.B: [new AC]", "Update Section 3.2 of Architecture Document as follows: [new/modified text or diagram description]").
- Present the complete draft of the "Sprint Change Proposal" to the user for final review and feedback. Incorporate any final adjustments requested by the user.

### 5. Finalize & Determine Next Steps

#### Approval Protocol:

1. **Final Review Checklist**
   - [ ] All changes clearly documented
   - [ ] Risk assessments complete
   - [ ] Rollback plans defined
   - [ ] Dependencies mapped
   - [ ] Timeline impacts assessed

2. **Approval Requirements**
   ```
   Sprint Change Proposal Approval
   
   I have reviewed the proposed changes and:
   [ ] Understand the impact on current sprint
   [ ] Accept the risk assessments
   [ ] Approve the implementation approach
   [ ] Acknowledge timeline adjustments
   
   Type 'APPROVE' to confirm or 'REVISE' to modify:
   ```

3. **Post-Approval Actions**
   
   **For Direct Implementation (<20% scope impact):**
   - Generate implementation checklist
   - Create tracking tickets
   - Update sprint backlog
   - Notify affected team members
   - Schedule progress checkpoints
   
   **For Major Changes (>20% scope impact):**
   - Escalation notice generated
   - PM/Architect handoff package created
   - Stakeholder notification drafted
   - Emergency sprint planning triggered
   - Architecture review scheduled

4. **Handoff Packages**
   
   **PO/SM Handoff:**
   ```markdown
   ## Backlog Update Package
   - Change summary
   - Story modifications list
   - Priority adjustments
   - Sprint impact analysis
   - Recommended actions
   ```
   
   **PM/Architect Handoff:**
   ```markdown
   ## Strategic Replan Package
   - Full impact analysis
   - Architectural implications
   - Risk assessment matrix
   - Alternative approaches
   - Stakeholder considerations
   ```

## Error Recovery Procedures

### Common Failure Scenarios:

1. **Checklist Load Failure**
   - Use embedded backup checklist
   - Proceed with core questions only
   - Document degraded analysis mode

2. **Artifact Access Issues**
   - List inaccessible artifacts
   - Proceed with available information
   - Flag incomplete analysis areas
   - Request manual artifact provision

3. **Impact Exceeds Threshold**
   - Automatic escalation triggered
   - Summary report generated
   - User notified of escalation
   - Await senior approval

4. **User Abandons Process**
   - Save progress to draft
   - Create resumption checkpoint
   - Document incomplete areas
   - Set reminder for follow-up

## Success Metrics

### Immediate Success Indicators:
- Change proposal completed within timeframe
- All impacts identified and documented
- Risk assessments validated
- User approval obtained

### Long-term Success Metrics:
- Implementation success rate >90%
- No surprise impacts discovered >95%
- Rollback required <5% of changes
- Stakeholder satisfaction >85%

## Continuous Improvement

### Feedback Collection:
1. Post-implementation review
2. Impact prediction accuracy
3. Change proposal clarity
4. Process efficiency metrics

### Improvement Actions:
- Refine impact assessment algorithms
- Update risk scoring models
- Enhance change templates
- Optimize approval workflows

### Review Triggers:
- Failed change implementation
- Missed impact identification
- Stakeholder complaints
- Process timeout exceeded

## Output Deliverables

### Primary Deliverable:
**Sprint Change Proposal** at `.ai/current/analysis/change-proposal-{date}.md`

Required sections:
1. **Executive Summary**
   - Change trigger and context
   - Impact scope (percentage of MVP affected)
   - Recommended approach
   - Risk level and mitigation

2. **Detailed Analysis**
   - Checklist completion record
   - Impact assessment by artifact
   - Dependency analysis
   - Risk matrix

3. **Proposed Changes**
   - Specific edits by artifact
   - Implementation sequence
   - Rollback procedures
   - Success criteria

4. **Appendices**
   - Decision log
   - Risk assessments
   - Alternative approaches considered
   - Stakeholder impacts

### Secondary Deliverables:
- **Annotated Change Checklist**: `.ai/current/analysis/change-checklist-completed-{date}.md`
- **Risk Register**: `.ai/current/analysis/change-risks-{date}.md`
- **Implementation Guide**: `.ai/current/analysis/change-implementation-{date}.md`

### Quality Standards:
- Clear, actionable language
- Specific line-by-line changes
- Comprehensive risk coverage
- Traceable decision rationale
- Measurable success criteria
