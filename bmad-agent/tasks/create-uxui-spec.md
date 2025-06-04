# Create UI/UX Specification Task

## CRITICAL SAFETY RULES ⚠️

**MANDATORY COMPLIANCE - NO EXCEPTIONS**

1. **User-Centered Design Gate**: NEVER proceed without:
   - Clear target user personas defined
   - User needs explicitly validated
   - Accessibility requirements confirmed
   - User approval of design direction

2. **Design Decision Rules**: EVERY UI/UX choice MUST have:
   - User research or feedback backing
   - Accessibility compliance verified
   - Multiple options presented when viable
   - Explicit user selection documented

3. **Quality Gates**: MANDATORY checkpoints at:
   - 25%: User personas and goals approved
   - 50%: Information architecture validated
   - 75%: User flows and wireframes reviewed
   - 100%: Complete spec with accessibility audit

4. **AI Safety Rules**:
   - NEVER assume user preferences without asking
   - ALWAYS present multiple design options
   - PROHIBIT skipping accessibility requirements
   - REQUIRE user testing plan inclusion

5. **Error Recovery**: If ANY safety rule is violated:
   - STOP the design process
   - Document the issue clearly
   - Present recovery options
   - Await user guidance

## Purpose

To collaboratively work with the user to define and document the User Interface (UI) and User Experience (UX) specifications for the project. This involves understanding user needs, defining information architecture, outlining user flows, and ensuring a solid foundation for visual design and frontend development. The output will populate a new document at `.ai/current/specs/frontend-spec.md` following the `front-end-spec-tmpl` template.

## Progressive Disclosure Phases

### Phase 1: Discovery (0-25%) 🔍
**Goal**: Understand users and establish design foundation

**Entry Criteria**:
- PRD and Project Brief available
- User ready to define UX goals
- Time allocated for collaborative design

**Activities**:
1. User persona development
2. Usability goals definition
3. Design principles establishment
4. Accessibility requirements setting

**Exit Criteria**:
- Personas documented and approved
- Design principles agreed
- Accessibility level confirmed
- 25% quality gate passed

### Phase 2: Structure (25-50%) 🏗️
**Goal**: Define information architecture and navigation

**Entry Criteria**:
- Phase 1 completed and approved
- User goals clearly understood

**Activities**:
1. Site map creation
2. Navigation structure design
3. Content hierarchy definition
4. Key screen identification

**Exit Criteria**:
- IA diagram approved
- Navigation patterns selected
- Screen inventory complete
- 50% quality gate passed

### Phase 3: Flow Design (50-75%) 🌊
**Goal**: Map user journeys and interactions

**Entry Criteria**:
- Phase 2 completed and approved
- Key screens identified

**Activities**:
1. Critical user flow mapping
2. Interaction pattern design
3. Error state definition
4. Wireframe conceptualization

**Exit Criteria**:
- User flows documented
- Interaction patterns approved
- Error handling defined
- 75% quality gate passed

### Phase 4: Specification (75-100%) 📝
**Goal**: Complete detailed UI/UX documentation

**Entry Criteria**:
- Phase 3 completed and approved
- All major design decisions made

**Activities**:
1. Component library planning
2. Style guide basics
3. Responsiveness strategy
4. Final specification assembly

**Exit Criteria**:
- Complete frontend-spec.md
- All sections reviewed
- Accessibility validated
- Ready for implementation

## Inputs

- Project Brief (`.ai/current/specs/project-brief.md` or equivalent)
- Product Requirements Document (PRD) (`.ai/current/specs/prd.md`)
- User feedback or research (if available)

## Key Activities & Instructions

### 1. Understand Core Requirements

- Review Project Brief and PRD to grasp project goals, target audience, key features, and any existing constraints.
- Ask clarifying questions about user needs, pain points, and desired outcomes.

### 2. Define Overall UX Goals & Principles (for `front-end-spec-tmpl`)

- Collaboratively establish and document:
  - Target User Personas (elicit details or confirm existing ones).
  - Key Usability Goals.
  - Core Design Principles for the project.

### 3. Develop Information Architecture (IA) (for `front-end-spec-tmpl`)

- Work with the user to create a Site Map or Screen Inventory.
- Define the primary and secondary Navigation Structure.
- Use Mermaid diagrams or lists as appropriate for the template.

### 4. Outline Key User Flows (for `front-end-spec-tmpl`)

- Identify critical user tasks from the PRD/brief.
- For each flow:
  - Define the user's goal.
  - Collaboratively map out the steps (use Mermaid diagrams or detailed step-by-step descriptions).
  - Consider edge cases and error states.

### 5. Discuss Wireframes & Mockups Strategy (for `front-end-spec-tmpl`)

- Clarify where detailed visual designs will be created (e.g., Figma, Sketch) and ensure the `front-end-spec-tmpl` correctly links to these primary design files.
- If low-fidelity wireframes are needed first, offer to help conceptualize layouts for key screens.

### 6. Define Component Library / Design System Approach (for `front-end-spec-tmpl`)

- Discuss if an existing design system will be used or if a new one needs to be developed.
- If new, identify a few foundational components to start with (e.g., Button, Input, Card) and their key states/behaviors at a high level. Detailed technical specs will be in `front-end-architecture`.

### 7. Establish Branding & Style Guide Basics (for `front-end-spec-tmpl`)

- If a style guide exists, link to it.
- If not, collaboratively define placeholders for: Color Palette, Typography, Iconography, Spacing.

### 8. Specify Accessibility (AX) Requirements (for `front-end-spec-tmpl`)

- Determine the target compliance level (e.g., WCAG 2.1 AA).
- List any known specific AX requirements.

### 9. Define Responsiveness Strategy (for `front-end-spec-tmpl`)

- Discuss and document key Breakpoints.
- Describe the general Adaptation Strategy.

### 10. Output Generation & Iterative Refinement (Guided by `front-end-spec-tmpl`)

- **a. Draft Section:** Incrementally populate one logical section of the frontend specification document (to be created at `.ai/current/specs/frontend-spec.md`) based on your discussions.
- **b. Present & Incorporate Initial Feedback:** Present the drafted section to the user for review. Discuss, explain and incorporate their initial feedback and revisions directly.
- **c. [Offer Advanced Self-Refinement & Elicitation Options](#offer-advanced-self-refinement--elicitation-options)**

## Offer Advanced Self-Refinement & Elicitation Options

(This section is called when needed prior to this)

Present the user with the following list of 'Advanced Reflective, Elicitation & Brainstorming Actions'. Explain that these are optional steps to help ensure quality, explore alternatives, and deepen the understanding of the current section before finalizing it and moving on. The user can select an action by number, or choose to skip this and proceed to finalize the section.

"To ensure the quality of the current section: **[Specific Section Name]** and to ensure its robustness, explore alternatives, and consider all angles, I can perform any of the following actions. Please choose a number (8 to finalize and proceed):

**Advanced Reflective, Elicitation & Brainstorming Actions I Can Take:**

{Instruction for AI Agent: Display the title of each numbered item below. If the user asks what a specific option means, provide a brief explanation of the action you will take, drawing from detailed descriptions tailored for the context.}

1.  **Critical Self-Review & User Goal Alignment**
2.  **Generate & Evaluate Alternative Design Solutions**
3.  **User Journey & Interaction Stress Test (Conceptual)**
4.  **Deep Dive into Design Assumptions & Constraints**
5.  **Usability & Accessibility Audit Review & Probing Questions**
6.  **Collaborative Ideation & UI Feature Brainstorming**
7.  **Elicit 'Unforeseen User Needs' & Future Interaction Questions**
8.  **Finalize this Section and Proceed.**

After I perform the selected action, we can discuss the outcome and decide on any further revisions for this section."

REPEAT by Asking the user if they would like to perform another Reflective, Elicitation & Brainstorming Action UNTIL the user indicates it is time to proceed to the next section (or selects #8)

## Error Recovery Procedures

### Common Failure Scenarios

1. **Unclear User Needs**
   - **Detection**: Conflicting requirements or vague goals
   - **Recovery**: Conduct user research session
   - **Prevention**: Start with persona validation

2. **Accessibility Violations**
   - **Detection**: Design choices exclude users
   - **Recovery**: Redesign with inclusive principles
   - **Prevention**: Check each decision against WCAG

3. **Information Overload**
   - **Detection**: Complex navigation or cluttered layouts
   - **Recovery**: Simplify and prioritize content
   - **Prevention**: Regular cognitive load assessment

4. **Platform Conflicts**
   - **Detection**: Design doesn't work across devices
   - **Recovery**: Adjust responsive strategy
   - **Prevention**: Mobile-first approach

### Recovery Protocol
1. **Pause** current design work
2. **Assess** the specific issue
3. **Present** alternative approaches
4. **Test** proposed solutions conceptually
5. **Validate** with user before proceeding
6. **Document** lessons learned

## Success Metrics

### Quantitative Metrics
- **Design Approval Rate**: >90% first-time approval
- **Accessibility Score**: 100% WCAG compliance
- **User Flow Efficiency**: <5 steps for key tasks
- **Component Reusability**: >70% shared components

### Qualitative Metrics
- **Clarity**: Users understand navigation instantly
- **Consistency**: Uniform patterns throughout
- **Delight**: Positive emotional response
- **Inclusivity**: Works for all user groups

### Early Warning Indicators
- User confusion about navigation
- Multiple iterations on same element
- Accessibility concerns raised
- Technical feasibility questions

## Continuous Improvement

### Post-Design Review
1. **Gather Feedback**:
   - What resonated with users?
   - What caused confusion?
   - What was missing?

2. **Analyze Patterns**:
   - Common design preferences
   - Recurring usability issues
   - Successful UI patterns

3. **Evolve Process**:
   - Update persona templates
   - Refine flow diagrams
   - Enhance accessibility checks

### Knowledge Capture
- Document successful UI patterns
- Record user preference trends
- Note accessibility solutions
- Build design system library

### Process Optimization
- Track design iteration cycles
- Measure user satisfaction
- Monitor implementation ease
- Improve collaboration methods
