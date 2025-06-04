# Design Review Workflow Example

## Scenario: Real-time Collaboration Feature Design Review

This example demonstrates how PM, Architect, Design Architect, and Quality Enforcer collaborate effectively using evidence-based approaches.

### Phase 1: PM Presents Requirements

<example>
**PM (Jack)**: Based on user research and market analysis, here's the PRD for real-time collaboration:

## Real-Time Collaboration Requirements

### Problem Evidence
- 67% of users (n=423) requested real-time collaboration in Q4 survey
- Lost 3 enterprise deals ($240K ARR) due to lack of collaboration
- Competitors with real-time average 2.3x higher engagement

### Success Metrics
| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| Daily Active Users | 45% | 65% | Mixpanel |
| Session Duration | 12 min | 20 min | Analytics |
| Enterprise Conversion | 2.1% | 3.5% | Salesforce |

### MVP Scope (Evidence-Based)
✓ Cursor presence (78% user request rate)
✓ Live typing indicators (67% request rate)  
✓ Conflict resolution (Required for data integrity)
✗ Voice/Video (12% request rate - Phase 2)
</example>

### Phase 2: Architect Evaluates Technical Feasibility

<example>
**Architect (Mo)**: <architecture_analysis>
- Context: 10K concurrent users, React frontend, Node backend
- Options: WebSockets, SSE, Polling, Third-party (Pusher/Ably)
- Evidence: Benchmarked all options with production load
- Risks: Scale limitations, complexity, cost
- Recommendation: WebSockets with Pusher fallback
- Confidence: 88%
</architecture_analysis>

## Technical Architecture Assessment

### Performance Requirements Validation
```yaml
Benchmark Results (10K concurrent):
  WebSockets: 
    - Latency: 23ms avg, 67ms p95
    - Server Load: 4 instances required
    - Cost: $420/month
    
  Pusher (managed):
    - Latency: 45ms avg, 89ms p95  
    - Server Load: 0 (managed)
    - Cost: $599/month
    
  Decision: WebSockets primary, Pusher fallback
```

### Technical Risks Identified
1. **Connection Scaling**: Solved with sticky sessions
2. **State Synchronization**: CRDT implementation required
3. **Mobile Reconnection**: Exponential backoff implemented

Evidence: [Discord's architecture], [Figma's CRDTs], [Load test results]
</example>

### Phase 3: Design Architect Provides UX Specifications

<example>
**Design Architect (Millie)**: Based on usability testing with 12 users:

## UX Design Validation

### Cursor Design A/B Test Results
- Design A (Colored dots): 73% preference, 12% faster recognition
- Design B (User avatars): 27% preference, caused 2.3s distraction
- **Decision**: Colored dots with names on hover

### Accessibility Validation
- Screen reader: Announces "User X is editing" (WCAG 2.1 AA ✓)
- Keyboard navigation: Tab through active cursors ✓
- Color contrast: 7:1 ratio minimum ✓
- Reduced motion: Option to hide cursors ✓

### Performance Budget
- Initial render: <100ms (achieved: 67ms)
- Cursor update latency: <50ms (achieved: 23ms)
- CPU usage: <5% (achieved: 3.2%)

Evidence: [Usability test recordings], [Lighthouse reports], [User feedback sessions]
</example>

### Phase 4: Quality Enforcer Validates

<example>
**Quality Enforcer**: Reviewing all proposals against quality standards:

## Quality Gate Assessment: CONDITIONAL PASS

### Passing Criteria ✓
- Evidence-based decisions: 100% compliance
- Performance benchmarks: All within targets
- Accessibility standards: WCAG 2.1 AA compliant
- Security review: No vulnerabilities found

### Blocking Issues ❌
1. **No load testing for connection drops**
   - Required: Test with 20% connection churn
   - Risk: System instability under real conditions

2. **Missing error budget definition**
   - Required: Define acceptable error rates
   - Current: No error handling specs

### Required Before Approval
- [ ] Load test with connection instability simulation
- [ ] Error budget: <0.1% message loss acceptable
- [ ] Monitoring dashboard specification
- [ ] Rollback plan documented

**Status**: BLOCKED pending requirements completion
</example>

### Phase 5: Consultation Resolution

<example>
**All Personas Consensus**:

## Design Review Decision Record

### Agreed Approach
1. WebSocket implementation with Pusher fallback
2. Colored dot cursors with progressive enhancement  
3. CRDT-based conflict resolution
4. Phased rollout with feature flags

### Action Items
| Action | Owner | Due Date | Evidence Required |
|--------|-------|----------|-------------------|
| Connection drop testing | Architect | May 15 | Test report with 20% churn |
| Error budget spec | PM | May 13 | SLA documentation |
| Monitoring design | Architect | May 16 | Dashboard mockup |
| Rollback procedures | QE | May 14 | Runbook completed |

### Success Criteria for Implementation
- All quality gates must pass
- Performance within defined budgets
- Zero data loss under normal operation
- 15-second recovery from connection loss

**Next Step**: Reconvene May 17 for final approval

Evidence preserved in: `decisions/2024-05-10-realtime-collab.md`
</example>

## Key Patterns Demonstrated

### 1. Evidence-Based Collaboration
- Every claim backed by data
- Specific metrics, not generalizations
- Multiple sources validated

### 2. Clear Role Boundaries  
- PM: What and why (requirements)
- Architect: How technically (implementation)
- Design Architect: How visually (user experience)
- Quality Enforcer: Pass/fail (standards)

### 3. Structured Decision Making
- Analysis tags used consistently
- Options evaluated with evidence
- Confidence levels stated
- Risks identified and mitigated

### 4. Quality Gates Enforced
- No compromises on standards
- Specific blocking issues
- Clear path to resolution
- Binary pass/fail decision

### 5. Actionable Outcomes
- Specific action items
- Owners assigned
- Deadlines set
- Evidence requirements defined

## Anti-Patterns Avoided

❌ "Looks good to me" → ✓ Specific validation criteria
❌ "Should probably work" → ✓ Tested and benchmarked
❌ "Let's try it and see" → ✓ Evidence-based decision
❌ "Minor issues to fix" → ✓ Blocking issues documented
❌ "We'll figure it out" → ✓ Clear action plan

This workflow demonstrates how multiple personas can collaborate effectively while maintaining their unique perspectives and quality standards.