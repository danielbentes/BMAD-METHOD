# Create Next Story Task

## CRITICAL SAFETY RULES ⚠️

**MANDATORY COMPLIANCE - NO EXCEPTIONS**

1. **Prerequisite Validation**: NEVER create a story when:
   - Previous story in sequence is incomplete
   - Story dependencies are not satisfied
   - Required documentation is missing
   - User hasn't approved override

2. **Context Completeness**: EVERY story MUST include:
   - All technical guidance from architecture docs
   - Complete acceptance criteria from epics
   - Verified API contracts and data models
   - Clear implementation path

3. **Quality Gates**: MANDATORY checkpoints at:
   - 25%: Story identification and validation
   - 50%: Technical context gathering complete
   - 75%: Story draft with all sections
   - 100%: Checklist validation passed

4. **AI Safety Rules**:
   - NEVER skip dependency verification
   - ALWAYS use Index Doc for navigation
   - PROHIBIT creating stories with gaps
   - REQUIRE explicit override for warnings

5. **Error Recovery**: If ANY safety rule is violated:
   - HALT story creation immediately
   - Document what's missing/wrong
   - Present clear options to user
   - Wait for explicit direction

## Purpose

To identify the next logical story based on project progress and epic definitions, and then to prepare a comprehensive, self-contained, and actionable story file using the `Story Template`. This task ensures the story is enriched with all necessary technical context, requirements, and acceptance criteria, making it ready for efficient implementation by a Developer Agent with minimal need for additional research.

## Progressive Disclosure Phases

### Phase 1: Discovery (0-25%) 🔍
**Goal**: Identify and validate next story

**Entry Criteria**:
- Access to all project documentation
- Story directory structure exists
- User ready to proceed

**Activities**:
1. Scan story directory for latest
2. Verify completion status
3. Check epic sequence
4. Validate prerequisites

**Exit Criteria**:
- Next story identified
- Prerequisites confirmed met
- User approved selection
- 25% quality gate passed

### Phase 2: Context Gathering (25-50%) 📚
**Goal**: Collect all implementation details

**Entry Criteria**:
- Story identified and validated
- All source docs accessible

**Activities**:
1. Extract epic requirements
2. Gather architectural context
3. Collect API specifications
4. Compile UI/UX requirements

**Exit Criteria**:
- All contexts documented
- No information gaps
- Technical details verified
- 50% quality gate passed

### Phase 3: Story Assembly (50-75%) 🔨
**Goal**: Create comprehensive story document

**Entry Criteria**:
- All context gathered
- Template available

**Activities**:
1. Populate story template
2. Write technical guidance
3. Define detailed tasks
4. Add implementation notes

**Exit Criteria**:
- Story draft complete
- All sections filled
- Tasks mapped to ACs
- 75% quality gate passed

### Phase 4: Validation (75-100%) ✅
**Goal**: Ensure story quality and completeness

**Entry Criteria**:
- Story draft complete
- Checklist available

**Activities**:
1. Run story draft checklist
2. Verify dev guidance clarity
3. Confirm no missing context
4. Get user approval

**Exit Criteria**:
- Checklist 100% passed
- User approved story
- Ready for development
- Story saved to active/

## Inputs for this Task

- Access to the project's documentation repository, specifically:
  - Index Doc (`.ai/current/specs/index.md`)
  - All Epic files (e.g., `.ai/current/specs/epic-{n}.md` - hereafter "Epic Files")
  - Existing story files in `.ai/current/work/stories/`
  - Main PRD (`.ai/current/specs/prd.md` - hereafter "PRD Doc")
  - Main Architecture Document (`.ai/current/specs/architecture.md` - hereafter "Main Arch Doc")
  - Frontend Architecture Document (`.ai/current/specs/frontend-architecture.md` - hereafter "Frontend Arch Doc," if relevant)
  - Project Structure Guide (`.ai/current/specs/project-structure.md`)
  - Operational Guidelines Document (`.ai/current/specs/operational-guidelines.md`)
  - Technology Stack Document (`.ai/current/specs/tech-stack.md`)
  - Data Models Document (`.ai/current/specs/data-models.md`)
  - API Reference Document (`.ai/current/specs/api-reference.md`)
  - UI/UX Specifications, Style Guides, Component Guides (`.ai/current/specs/frontend-spec.md` and related files)
- The `bmad-agent/templates/story-tmpl.md` (hereafter "Story Template")
- The `bmad-agent/checklists/story-draft-checklist.md` (hereafter "Story Draft Checklist")
- User confirmation to proceed with story identification and, if needed, to override warnings about incomplete prerequisite stories.

## Task Execution Instructions

### 1. Identify Next Story for Preparation

- Review `.ai/current/work/stories/` (all subdirectories: `active/`, `review/`, `done/`) to find the highest-numbered story file.
- **If a highest story file exists (`{lastEpicNum}.{lastStoryNum}.story.md`):**

  - Verify its `Status` is 'Done' (or equivalent).
  - If not 'Done', present an alert to the user:

    ```
    ALERT: Found incomplete story:
    File: {lastEpicNum}.{lastStoryNum}.story.md
    Status: [current status]

    Would you like to:
    1. View the incomplete story details (instructs user to do so, agent does not display)
    2. Cancel new story creation at this time
    3. Accept risk & Override to create the next story in draft

    Please choose an option (1/2/3):
    ```

  - Proceed only if user selects option 3 (Override) or if the last story was 'Done'.
  - If proceeding: Check the Epic File for `{lastEpicNum}` for a story numbered `{lastStoryNum + 1}`. If it exists and its prerequisites (per Epic File) are met, this is the next story.
  - Else (story not found or prerequisites not met): The next story is the first story in the next Epic File (e.g., `.ai/current/specs/epic-{lastEpicNum + 1}.md`, then `epic-{lastEpicNum + 2}.md`, etc.) whose prerequisites are met.

- **If no story files exist in `.ai/current/work/stories/`:**
  - The next story is the first story in `.ai/current/specs/epic-1.md` (then `.ai/current/specs/epic-2.md`, etc.) whose prerequisites are met.
- If no suitable story with met prerequisites is found, report to the user that story creation is blocked, specifying what prerequisites are pending. HALT task.
- Announce the identified story to the user: "Identified next story for preparation: {epicNum}.{storyNum} - {Story Title}".

### 2. Gather Core Story Requirements (from Epic File)

- For the identified story, open its parent Epic File.
- Extract: Exact Title, full Goal/User Story statement, initial list of Requirements, all Acceptance Criteria (ACs), and any predefined high-level Tasks.
- Keep a record of this original epic-defined scope for later deviation analysis.

### 3. Gather & Synthesize In-Depth Technical Context for Dev Agent

- <critical_rule>Systematically use the Index Doc (`.ai/current/specs/index.md`) as your primary guide to discover paths to ALL detailed documentation relevant to the current story's implementation needs.</critical_rule>
- Thoroughly review the PRD Doc, Main Arch Doc, and Frontend Arch Doc (if a UI story).
- Guided by the Index Doc and the story's needs, locate, analyze, and synthesize specific, relevant information from sources such as:
  - Data Models Doc (structure, validation rules).
  - API Reference Doc (endpoints, request/response schemas, auth).
  - Applicable architectural patterns or component designs from Arch Docs.
  - UI/UX Specs, Style Guides, Component Guides (for UI stories).
  - Specifics from Tech Stack Doc if versions or configurations are key for this story.
  - Relevant sections of the Operational Guidelines Doc (e.g., story-specific error handling nuances, security considerations for data handled in this story).
- The goal is to collect all necessary details the Dev Agent would need, to avoid them having to search extensively. Note any discrepancies between the epic and these details for "Deviation Analysis."

### 4. Verify Project Structure Alignment

- Cross-reference the story's requirements and anticipated file manipulations with the Project Structure Guide (and frontend structure if applicable).
- Ensure any file paths, component locations, or module names implied by the story align with defined structures.
- Document any structural conflicts, necessary clarifications, or undefined components/paths in a "Project Structure Notes" section within the story draft.

### 5. Populate Story Template with Full Context

- Create a new story file: `.ai/current/work/stories/active/{epicNum}.{storyNum}.story.md`.
- Use the Story Template to structure the file.
- Fill in:
  - Story `{EpicNum}.{StoryNum}: {Short Title Copied from Epic File}`
  - `Status: Draft`
  - `Story` (User Story statement from Epic)
  - `Acceptance Criteria (ACs)` (from Epic, to be refined if needed based on context)
- **`Dev Technical Guidance` section (CRITICAL):**
  - Based on all context gathered (Step 3 & 4), embed concise but critical snippets of information, specific data structures, API endpoint details, precise references to _specific sections_ in other documents (e.g., "See `Data Models Doc#User-Schema-ValidationRules` for details"), or brief explanations of how architectural patterns apply to _this story_.
  - If UI story, provide specific references to Component/Style Guides relevant to _this story's elements_.
  - The aim is to make this section the Dev Agent's primary source for _story-specific_ technical context.
- **`Tasks / Subtasks` section:**
  - Generate a detailed, sequential list of technical tasks and subtasks the Dev Agent must perform to complete the story, informed by the gathered context.
  - Link tasks to ACs where applicable (e.g., `Task 1 (AC: 1, 3)`).
- Add notes on project structure alignment or discrepancies found in Step 4.
- Prepare content for the "Deviation Analysis" based on discrepancies noted in Step 3.

### 6. Run Story Draft Validation

- Execute the Story Draft Checklist against the populated story.
- For any failed items:
  - Document the gap
  - Attempt to resolve if possible
  - Flag for user attention if not
- Only proceed when checklist passes or user approves exceptions.

### 7. Present Story for Approval

- Show user the story summary with:
  - Story ID and title
  - Prerequisite status
  - Key technical elements included
  - Any deviations or concerns
- Request explicit approval to finalize

### 8. Finalize and Save

- Upon approval, ensure story is saved in `.ai/current/work/stories/active/`
- Confirm file creation and accessibility
- Provide user with story location and next steps

## Error Recovery Procedures

### Common Failure Scenarios

1. **Incomplete Prerequisites**
   - **Detection**: Required stories not done
   - **Recovery**: List blocking stories, await direction
   - **Prevention**: Check dependencies first

2. **Missing Documentation**
   - **Detection**: Referenced docs not found
   - **Recovery**: List missing docs, request creation
   - **Prevention**: Validate all docs upfront

3. **Context Gaps**
   - **Detection**: Technical details unavailable
   - **Recovery**: Flag gaps, seek clarification
   - **Prevention**: Thorough context gathering

4. **Epic Misalignment**
   - **Detection**: Story doesn't match epic definition
   - **Recovery**: Reconcile with user input
   - **Prevention**: Strict epic adherence

### Recovery Protocol
1. **Stop** at point of failure
2. **Document** what's missing/wrong
3. **Present** clear options to user
4. **Wait** for explicit direction
5. **Resume** only when issue resolved
6. **Verify** fix before continuing

## Success Metrics

### Quantitative Metrics
- **Story Completeness**: 100% sections filled
- **Checklist Pass Rate**: >95% first attempt
- **Dev Guidance Quality**: Zero clarification requests
- **Dependency Accuracy**: 100% prerequisites met

### Qualitative Metrics
- **Clarity**: Developer can start immediately
- **Completeness**: No research needed by dev
- **Accuracy**: All technical details correct
- **Traceability**: Clear links to source docs

### Early Warning Indicators
- Multiple missing documents
- Unclear epic definitions
- Conflicting technical guidance
- Incomplete prerequisite stories

## Continuous Improvement

### Post-Story Review
1. **Track Implementation**:
   - Was guidance sufficient?
   - What questions arose?
   - What was missing?

2. **Analyze Patterns**:
   - Common missing elements
   - Frequent clarifications
   - Successful story patterns

3. **Improve Process**:
   - Enhance context gathering
   - Refine task generation
   - Update checklists

### Knowledge Capture
- Document story creation patterns
- Record common technical contexts
- Note successful task breakdowns
- Build story quality metrics

### Process Optimization
- Track story creation time
- Monitor dev success rate
- Measure rework frequency
- Optimize template usage
