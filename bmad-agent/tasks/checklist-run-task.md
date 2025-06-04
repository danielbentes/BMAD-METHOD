# Checklist Validation Task

## CRITICAL SAFETY RULES - MANDATORY COMPLIANCE

### STOP CONDITIONS - ABORT IMMEDIATELY IF:
- Checklist file corrupted or missing
- Required documents contain merge conflicts
- Validation would expose sensitive data
- Previous validation shows systematic failures (>80% fail rate)
- User explicitly states "skip validation" or "ignore checklist"

### MANDATORY VALIDATIONS BEFORE PROCEEDING:
1. **Checklist Integrity**: Verify checklist file exists and is readable
2. **Document Availability**: Confirm all required documents accessible
3. **Permission Check**: Ensure read access to all resources
4. **Quality Threshold**: Previous validations must show <50% critical failures
5. **User Intent**: Confirm user wants thorough validation, not just quick review

### QUALITY GATES - MUST PASS ALL:
- [ ] Valid checklist file identified and loaded
- [ ] All required documents located or alternatives provided
- [ ] No corruption in checklist or document files
- [ ] User confirmed validation approach (interactive/YOLO)
- [ ] Output directory writable for validation report

## Purpose

This task provides instructions for validating documentation against checklists. The agent should follow these instructions to ensure thorough and systematic validation of documents.

## Context

The BMAD Method uses various checklists to ensure quality and completeness of different artifacts. The mapping between checklists and their required documents is defined in `checklist-mappings`. This allows for easy addition of new checklists without modifying this task.

## Progressive Disclosure Phases

### Phase 1: Checklist Selection (MANDATORY)
1. Load and validate checklist-mappings.yml
2. Present available checklists to user
3. Confirm checklist selection
4. Verify checklist file integrity
5. **GATE**: Valid checklist selected → Continue to Phase 2

### Phase 2: Document Discovery
1. Identify required documents from mapping
2. Search default locations systematically
3. Request missing document locations from user
4. Validate document accessibility
5. **GATE**: All documents available → Continue to Phase 3

### Phase 3: Validation Execution
1. Choose validation mode (interactive/YOLO)
2. Process checklist items systematically
3. Document findings with evidence
4. Calculate metrics and scores
5. **GATE**: Validation complete → Continue to Phase 4

### Phase 4: Report Generation
1. Compile comprehensive findings
2. Generate actionable recommendations
3. Save validation report
4. Present summary to user
5. **FINAL GATE**: Report accepted → Task Complete

## Instructions

### 1. Initial Assessment with Safety Checks

#### Checklist Discovery Protocol:
1. **Load Mapping File**
   - Attempt to read `checklist-mappings.yml`
   - Validate YAML structure integrity
   - Handle missing file gracefully

2. **Checklist Selection Logic**
   - If user provides a checklist name:
     - Look for exact match in checklist-mappings.yml
     - If no exact match, try fuzzy matching with confirmation
     - If multiple matches found, present options with descriptions
     - Once matched, validate checklist_file path exists
   - If no checklist specified:
     - Present available checklists with clear descriptions
     - Group by category (architecture, frontend, PM, story)
     - Require explicit selection

3. **Mode Selection**
   - Explain validation modes clearly:
     - **Interactive**: Section-by-section review with discussion
     - **YOLO**: Complete analysis in one pass
   - Default to Interactive for first-time validations
   - Record user preference for future sessions

#### Error Handling:
- **Missing Mapping File**: Provide manual checklist selection
- **Invalid YAML**: Report specific parsing errors
- **Ambiguous Selection**: Show all matches with differences highlighted
- **Access Denied**: Provide troubleshooting steps

2. **Document Location**

   - Look up the required documents and default locations in `checklist-mappings`
   - For each required document:
     - Check all default locations specified in the mapping
     - If not found, ask the user for the document location
   - Verify all required documents are accessible

3. **Checklist Processing**

   If in interactive mode:

   - Work through each section of the checklist one at a time
   - For each section:
     - Review all items in the section
     - Check each item against the relevant documentation
     - Present findings for that section
     - Get user confirmation before proceeding to next section

   If in YOLO mode:

   - Process all sections at once
   - Create a comprehensive report of all findings
   - Present the complete analysis to the user

### 4. Validation Approach with Evidence Requirements

#### For Each Checklist Item:

1. **Requirement Analysis**
   - Parse requirement for key criteria
   - Identify measurable success indicators
   - Note any conditional applicability

2. **Evidence Gathering**
   - Search for explicit requirement coverage
   - Document specific file locations and line numbers
   - Capture relevant quotes or sections
   - Consider implicit coverage with justification

3. **Assessment Criteria**
   - ✅ **PASS**: 
     - Requirement clearly met with evidence
     - Location: [file:line] with quote
     - Confidence: High (>90%)
   - ❌ **FAIL**: 
     - Requirement not met or insufficient
     - Missing elements documented
     - Improvement path identified
   - ⚠️ **PARTIAL**: 
     - Some aspects covered
     - Specific gaps identified
     - Completion percentage estimated
   - **N/A**: 
     - Clear justification required
     - Alternative coverage noted
     - User confirmation needed

4. **Evidence Standards**
   - Direct quotes preferred over paraphrasing
   - Multiple sources strengthen validation
   - Visual elements (diagrams) count as evidence
   - Code examples validate implementation items

5. **Section Analysis**

   For each section:

   - Calculate pass rate
   - Identify common themes in failed items
   - Provide specific recommendations for improvement
   - In interactive mode, discuss findings with user
   - Document any user decisions or explanations

6. **Final Report**

   Prepare a summary that includes:

   - Overall checklist completion status
   - Pass rates by section
   - List of failed items with context
   - Specific recommendations for improvement
   - Any sections or items marked as N/A with justification
   - Save the final report at `.ai/quality/validations/checklist-{name}-{date}.md`

## Special Considerations

1. **Architecture Checklist**

   - Focus on technical completeness and clarity
   - Verify all system components are addressed
   - Check for security and scalability considerations
   - Ensure deployment and operational aspects are covered

2. **Frontend Architecture Checklist**

   - Validate UI/UX specifications
   - Check component structure and organization
   - Verify state management approach
   - Ensure responsive design considerations

3. **PM Checklist**

   - Focus on product requirements clarity
   - Verify user stories and acceptance criteria
   - Check market and user research coverage
   - Ensure technical feasibility is addressed

4. **Story Checklists**
   - Verify clear acceptance criteria
   - Check for technical context and dependencies
   - Ensure testability is addressed
   - Validate user value is clearly stated

## Success Criteria

### Validation Completion Requirements:
1. All applicable items assessed with evidence
2. Clear pass/fail status with confidence scores
3. Specific, actionable recommendations for all failures
4. User has reviewed and accepted findings
5. Final report includes all decisions and rationales
6. Validation results saved with proper naming convention

### Quality Metrics:
- **Coverage**: 100% of applicable items assessed
- **Evidence**: >95% of assessments have concrete evidence
- **Clarity**: All recommendations specific and actionable
- **Accuracy**: <5% false positive/negative rate

## Error Recovery Procedures

### Common Failure Scenarios:

1. **Checklist File Not Found**
   - Search alternative locations
   - Offer to use template checklist
   - Allow manual checklist input

2. **Document Access Denied**
   - Request alternative location
   - Offer to proceed with available documents
   - Document gaps in final report

3. **Validation Conflicts**
   - Present both interpretations
   - Request user clarification
   - Document decision rationale

4. **Report Save Failure**
   - Attempt alternative location
   - Provide copy-paste version
   - Email report option

## Continuous Improvement

### Metrics Tracking:
1. Average validation completion time
2. False positive/negative rates
3. User acceptance of findings
4. Recommendation implementation rate

### Feedback Integration:
- Collect user feedback on each validation
- Track which recommendations prove most valuable
- Identify common documentation gaps
- Refine checklist items based on outcomes

### Update Triggers:
- Repeated failures on specific items
- User feedback indicates confusion
- New document types introduced
- Process improvements identified

## Example Interaction

Agent: "Let me check the available checklists... According to checklist-mappings.yml, we have several options. Which would you like to use?"

User: "The architect checklist"

Agent: "Would you like to work through it section by section (interactive) or get a complete analysis all at once (YOLO mode)?"

User: "Interactive please"

Agent: "According to the mappings, I need to check for architecture.md. The default location is .ai/current/specs/architecture.md. Should I look there?"

[Continue interaction based on user responses...]
