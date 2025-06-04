# CRITICAL TASK: Product Requirements Document (PRD) Generation - Zero Ambiguity Protocol

## CRITICAL SAFETY RULES (MANDATORY COMPLIANCE)

### RULE 0 (MOST IMPORTANT): PRD Completeness Protocol
If ANY PRD section is incomplete or ambiguous, you MUST:
1. **HALT** progression to next section
2. **IDENTIFY** specific gaps or ambiguities
3. **COLLABORATE** with user to resolve
4. **VALIDATE** understanding before proceeding
5. **DOCUMENT** all decisions explicitly

**PENALTY**: Incomplete PRDs = -$5000 penalty + cascading project failures + mandatory requirements rewrite

### RULE 1: Zero Tolerance for Assumptions
**NEVER ALLOW** in PRDs:
- Undefined user needs or personas
- Vague success criteria ("better", "improved", "enhanced")
- Missing non-functional requirements
- Unquantified business value
- Technical implementation details (unless workflow B)
- Scope creep beyond MVP

### RULE 2: Evidence-Based Requirements
**ALL** requirements MUST have:
- User research or market validation
- Quantifiable success metrics
- Clear acceptance criteria
- Prioritization rationale
- Risk assessment
- Dependencies identified

### RULE 3: Epic and Story Quality
**EVERY** epic and story MUST:
- Follow user story format precisely
- Have 5-10 specific acceptance criteria
- Include edge cases and error scenarios
- Define measurable outcomes
- Maintain independence (INVEST)
- Support logical implementation sequence

### RULE 4: Stakeholder Alignment
**NO PRD** proceeds without:
- User confirmation at each section
- Technical feasibility acknowledgment
- Business value validation
- Resource availability check
- Timeline reasonability verification

### RULE 5: Quality Gate Compliance
**ALL** PRDs require:
- PM checklist 100% complete
- No TBD or placeholder content
- All sections evidence-backed
- Cross-references validated
- Handoff readiness confirmed

## PURPOSE (MANDATORY UNDERSTANDING)
Transform inputs into definitive product requirements that serve as the single source of truth for all downstream development. PRDs are the foundation—flaws here multiply exponentially through the project lifecycle.

## PRD GENERATION PHASES (PROGRESSIVE DISCLOSURE)

### Phase 0: Pre-Generation Setup (MANDATORY - 15 minutes)
**Before ANY content creation:**

#### Workflow Selection (CRITICAL DECISION)
```markdown
## WORKFLOW CHOICE (User MUST select):

A. **Outcome Focused (RECOMMENDED)**
   - PM defines WHAT (outcomes)
   - Architect defines HOW (implementation)
   - Clear separation of concerns
   - Notes capture technical nuances

B. **Very Technical (USE WITH CAUTION)**
   - PM defines WHAT + HOW
   - Detailed technical decisions in PRD
   - No architect involvement
   - Higher risk of suboptimal design
   
**SELECTED**: [User must explicitly choose]
```

#### Interaction Mode Selection
```markdown
## INTERACTION MODE (User MUST select):

1. **INCREMENTAL (RECOMMENDED)**
   - Section-by-section progression
   - Continuous validation
   - Lower error risk
   - Better alignment

2. **YOLO Mode (RISKY)**
   - Full draft generation
   - Single review cycle
   - Higher error risk
   - Faster but less accurate
```

#### Structured Thinking Requirement
**MANDATORY**: Complete <decision_analysis> tag before PRD creation:
```xml
<decision_analysis>
  <context>PRD creation for [product/feature]</context>
  <options>
    <option name="Technical approach A">...</option>
    <option name="Business approach B">...</option>
    <option name="Hybrid approach C">...</option>
  </options>
  <evidence>Market research, user feedback, technical constraints</evidence>
  <risks>Implementation complexity, timeline, resources</risks>
  <recommendation>Selected approach with rationale</recommendation>
  <confidence>85%+ required</confidence>
</decision_analysis>
```
**PENALTY**: Creating PRD without analysis = -$2000
   
**SELECTED**: [User must explicitly choose]
```

#### Input Validation Checklist
- [ ] Project brief available and reviewed
- [ ] User research/data accessible
- [ ] Technical constraints identified
- [ ] Business objectives clear
- [ ] Success metrics defined

**PHASE 0 GATE**: Cannot proceed without workflow and mode selection

### Phase 1: Foundation Sections (30-45 minutes)

#### Section 1.1: Problem Statement (MANDATORY)
**Requirements:**
- [ ] Specific problem articulated
- [ ] Impact quantified (users, revenue, time)
- [ ] Current state documented
- [ ] Root cause identified
- [ ] Evidence provided

**Quality Checks:**
```yaml
problem_validation:
  - specificity: NO_VAGUE_STATEMENTS
  - quantification: METRICS_REQUIRED
  - evidence: DATA_BACKED
  - scope: CLEARLY_BOUNDED
  - urgency: TIMELINE_DEFINED
```

#### Section 1.2: Goals & Success Metrics (CRITICAL)
**Requirements:**
- [ ] SMART goals defined
- [ ] Leading indicators identified
- [ ] Lagging indicators specified
- [ ] Measurement plan included
- [ ] Baseline established

**Validation Format:**
```markdown
Goal: [Specific measurable outcome]
Metric: [Exact measurement]
Current: [Baseline value]
Target: [Specific target with date]
Method: [How to measure]
```

#### Section 1.3: User Personas (EVIDENCE-BASED)
**Requirements:**
- [ ] Research-backed personas (not assumptions)
- [ ] Specific demographics and behaviors
- [ ] Jobs-to-be-done articulated
- [ ] Pain points validated
- [ ] User quotes included

**Anti-Pattern Check:**
- ❌ "General users"
- ❌ "Power users" without definition
- ❌ Assumption-based characteristics
- ✅ "Sarah, 34, Product Manager who checks analytics 5x daily"

**PHASE 1 GATE**: All foundation sections complete with evidence

### Phase 2: Scope Definition (45-60 minutes)

#### Section 2.1: MVP Scope (RUTHLESS PRIORITIZATION)
**Requirements:**
- [ ] Core features only (true minimum)
- [ ] Each feature tied to specific goal
- [ ] Technical dependencies mapped
- [ ] 3-month delivery target
- [ ] Post-MVP explicitly deferred

**MVP Validation Matrix:**
```markdown
| Feature | Goal Support | User Need | Technical Risk | In MVP? |
|---------|--------------|-----------|----------------|---------|
| [Name]  | [Which goal] | [Evidence]| [H/M/L]       | [Y/N]   |
```

#### Section 2.2: Technical Assumptions (ARCHITECT CRITICAL)
**Repository Structure Decision (MANDATORY):**
```markdown
## Repository Architecture Decision

**Options Evaluated:**
1. Monorepo: [Pros/Cons for this project]
2. Polyrepo: [Pros/Cons for this project]

**DECISION**: [Monorepo/Polyrepo]
**RATIONALE**: [Specific reasons with tradeoffs]
**IMPACT ON MVP**: [How this affects scope/timeline]
```

**Service Architecture Decision (MANDATORY):**
```markdown
## Service Architecture Decision

**Options Evaluated:**
1. Monolith: [Pros/Cons for this project]
2. Microservices: [Pros/Cons for this project]
3. Serverless: [Pros/Cons for this project]

**DECISION**: [Selected architecture]
**RATIONALE**: [Specific reasons with tradeoffs]
**SCALING PLAN**: [How to evolve post-MVP]
```

#### Section 2.3: Non-Functional Requirements (MEASURABLE)
**Requirements:**
- [ ] Performance targets (specific ms/fps)
- [ ] Availability SLA (specific %)
- [ ] Security requirements (specific standards)
- [ ] Accessibility level (WCAG specific)
- [ ] Browser/device support (specific list)

**PHASE 2 GATE**: Scope completely defined with no ambiguity

### Phase 3: Epic and Story Generation (60-90 minutes)

#### Pre-Generation Analysis (MANDATORY)
**Internal Planning Steps:**
1. Map all features to epics
2. Identify cross-cutting concerns
3. Determine logical dependencies
4. Sequence for implementation
5. Validate against MVP scope

#### Section 3.1: Epic Definition (STRATEGIC LEVEL)
**Epic Quality Requirements:**
- [ ] Clear business outcome
- [ ] 3-5 epics maximum for MVP
- [ ] No technical implementation
- [ ] Measurable completion criteria
- [ ] Priority order justified

**Epic Template:**
```markdown
## Epic: [Business Capability Name]
**Goal**: [Specific business outcome]
**Value**: [Quantified benefit]
**Success**: [How to measure completion]
**Priority**: [1-5 with rationale]
**Dependencies**: [Other epics/external factors]
```

#### Section 3.2: Story Generation (TACTICAL LEVEL)
**Story Quality Requirements:**
- [ ] Follows "As a... I want... So that..." format
- [ ] Independent and testable
- [ ] 5-10 acceptance criteria each
- [ ] Includes error scenarios
- [ ] Sequenced logically

**Story Validation Protocol:**
```markdown
## Story Dependency Analysis
Story X → Story Y because: [Specific dependency]
Parallel possible: [Yes/No with reason]
Blocking risk: [High/Medium/Low]
```

**Progressive Story Review (INCREMENTAL MODE):**
1. Present epic with all stories listed
2. Show proposed sequence with rationale
3. Get user approval on structure
4. Detail each story in sequence
5. Validate acceptance criteria completeness

**PHASE 3 GATE**: All stories validated and sequenced

### Phase 4: Integration Planning (30 minutes)

#### Section 4.1: External Dependencies
**Requirements:**
- [ ] All third-party services identified
- [ ] API requirements documented
- [ ] Data sources mapped
- [ ] Integration risks assessed
- [ ] Fallback plans defined

#### Section 4.2: Internal Handoffs
**Requirements:**
- [ ] Design → Development needs
- [ ] Backend → Frontend contracts
- [ ] Development → QA requirements
- [ ] DevOps deployment needs
- [ ] Documentation requirements

**PHASE 4 GATE**: All integrations and handoffs defined

### Phase 5: Quality Validation (30 minutes)

#### PM Checklist Execution (MANDATORY)
**Checklist Processing Protocol:**
1. Load `pm-checklist.md`
2. Evaluate EACH item systematically
3. Document evidence for compliance
4. Present section summaries to user
5. Address ALL deficiencies
6. Generate final compliance report

**Compliance Report Format:**
```markdown
## PRD Quality Compliance Report

### Section: [Name]
- Items Checked: X/Y
- Deficiencies Found: [List]
- Resolutions: [Actions taken]
- Final Status: [PASS/FAIL]

### Overall Compliance: XX%
### Blockers Remaining: [None/List]
```

#### Technical Handoff Preparation
**For UI Components:**
- [ ] Design requirements extracted
- [ ] Component inventory created
- [ ] Interaction patterns defined
- [ ] Responsive requirements noted
- [ ] Accessibility needs highlighted

**PHASE 5 GATE**: 100% checklist compliance achieved

## ADVANCED REFINEMENT OPTIONS

### Self-Refinement Protocol
At each section completion, offer:
1. **Depth Enhancement**: Add more detail/examples
2. **Scope Refinement**: Narrow or expand scope
3. **Risk Analysis**: Identify additional risks
4. **Alternative Approaches**: Explore other solutions
5. **Validation Strengthening**: Add more evidence

### Elicitation Techniques
When user input unclear:
1. **Specific Examples**: "Can you give me an example of..."
2. **Contrast Questions**: "Is it more like X or Y?"
3. **Boundary Testing**: "What would be out of scope?"
4. **Priority Forcing**: "If you could only have one..."
5. **Scenario Walking**: "Walk me through how..."

## ERROR HANDLING PROTOCOLS

### When Requirements Conflict
1. **DOCUMENT** both requirements
2. **IDENTIFY** the conflict explicitly
3. **ANALYZE** impact of each option
4. **FACILITATE** user decision
5. **RECORD** rationale clearly

### When Information Missing
1. **MARK** as [PENDING: specific info needed]
2. **ASSESS** if blocker for progression
3. **SUGGEST** reasonable defaults
4. **TRACK** for follow-up
5. **PREVENT** assumption creep

### When Scope Creeps
1. **IDENTIFY** scope expansion
2. **CALCULATE** impact on timeline
3. **PRESENT** trade-off options
4. **ENFORCE** MVP boundaries
5. **DOCUMENT** for post-MVP

## CONTINUOUS IMPROVEMENT

### After Each PRD
- Document what worked well
- Identify communication gaps
- Update templates if needed
- Refine estimation accuracy
- Strengthen weak sections

### Pattern Recognition
- Track common missing elements
- Identify recurring ambiguities
- Build example libraries
- Enhance validation rules
- Share learnings

## CRITICAL REMINDERS

1. **Your PRD is the foundation** - errors multiply downstream
2. **Ambiguity is the enemy** - be specific or ask
3. **Evidence beats opinion** - always require data
4. **Scope creep kills projects** - defend MVP boundaries
5. **Sequence matters** - logical order prevents rework

## WORKFLOW B: TECHNICAL PRD ADDITIONS

**ONLY if Workflow B selected:**

### Additional Section: Core Technical Decisions
```markdown
## [OPTIONAL: Simplified PM-to-Dev Workflow Only]
## Core Technical Decisions & Application Structure

### Technology Stack
**Backend**: [Language, framework, rationale]
**Frontend**: [Framework, rationale if applicable]
**Database**: [Type, specific system, rationale]
**Cache**: [System if needed, rationale]
**Queue**: [System if needed, rationale]

### Application Structure
**Architecture Pattern**: [MVC, hexagonal, etc.]
**Key Modules**:
- Module 1: [Purpose and responsibility]
- Module 2: [Purpose and responsibility]

### Deployment Target
**Platform**: [AWS/GCP/Azure/Self-hosted]
**Compute**: [Serverless/Containers/VMs]
**Rationale**: [Why these choices]

### Development Standards
**Testing**: [Unit test coverage target]
**Code Style**: [Linting standards]
**Documentation**: [Requirements]
```

Remember: The PRD is where precision prevents problems. Every ambiguity you allow creates exponential confusion downstream. Be thorough, be specific, be uncompromising on clarity.