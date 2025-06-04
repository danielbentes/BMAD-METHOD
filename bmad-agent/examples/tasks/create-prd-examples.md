# Create PRD Task Examples

## GOOD Examples: Evidence-Based PRD Creation

### Example 1: E-commerce Checkout Optimization PRD
<example>
user: Create a PRD for optimizing our checkout process

pm: [analyzes current checkout funnel data]
[reviews 43 user session recordings]
[examines competitor checkouts]
[conducts stakeholder interviews]

## Workflow Selection
**SELECTED**: A. Outcome Focused (PM defines WHAT, Architect defines HOW)
**Interaction Mode**: INCREMENTAL (section-by-section validation)

<decision_analysis>
- Context: 68% cart abandonment rate vs 55% industry average
- Options: Quick fixes, full redesign, progressive enhancement
- Evidence: 43 session recordings show friction at payment step
- Risks: Breaking existing integrations, losing customer trust
- Recommendation: Progressive enhancement approach
- Confidence: 92% based on A/B test potential
</decision_analysis>

# Checkout Optimization PRD

## Problem Statement
Current checkout process has 68% abandonment rate, 13 points above industry average, costing $2.4M annually in lost revenue. Analysis of 1,247 abandoned carts shows:
- 34% abandon at shipping calculation (avg 8 second wait)
- 28% abandon at account creation requirement  
- 19% abandon at payment due to limited options
- 19% other/unknown reasons

**Evidence**: Mixpanel funnel analysis, FullStory recordings, Baymard Institute benchmark

## Goals & Success Metrics

| Goal | Current | Target | Measurement | Timeline |
|------|---------|--------|-------------|----------|
| Reduce abandonment | 68% | 55% | Mixpanel funnel | 3 months |
| Increase conversion | 2.3% | 3.0% | GA4 e-commerce | 3 months |
| Decrease time to purchase | 4:32 | 3:00 | Session recordings | 2 months |
| Increase mobile conversion | 1.1% | 2.0% | GA4 segments | 3 months |

**Validation**: Each metric has automated dashboard, weekly review scheduled

## User Personas (Research-Backed)

### Primary: "Efficient Emma" (62% of users)
- Demographics: 25-40, urban, $50-100K income
- Behavior: Comparison shops, abandons for shipping costs
- Quote: "I had 3 items in cart but shipping made it not worth it"
- Evidence: 312 user interviews, behavioral clustering analysis

### Secondary: "Mobile Mike" (31% of users)  
- Demographics: 18-35, mobile-first, impulse buyer
- Behavior: Abandons due to form complexity on mobile
- Quote: "Creating an account on my phone is painful"
- Evidence: Device segmentation data, 89 mobile user interviews

## MVP Scope (13% Conversion Lift Projected)

### In Scope - Phase 1 (2 months)
✓ Real-time shipping calculation (address autocomplete)
✓ Guest checkout option (no account required)
✓ Apple Pay/Google Pay integration
✓ Progress indicator with time estimate
✓ Trust badges and security messaging

### Out of Scope - Phase 2
- Saved payment methods
- One-click reorder
- Subscription options
- B2B checkout flow

**Evidence**: Prioritization based on effort/impact matrix with eng estimates

## Technical Architecture Decision

**Repository**: Monorepo (frontend in existing repo)
**Rationale**: Shared component library, unified deployment
**Service Architecture**: API Gateway pattern
**Rationale**: Existing pattern, 50ms latency acceptable

## Acceptance Criteria Samples

### Story: Implement Guest Checkout
```gherkin
GIVEN a user with items in cart
WHEN they click "Checkout"
THEN they see "Checkout as Guest" option prominently (top 300px)
  AND clicking it bypasses account creation
  AND their email is requested but not required
  AND order confirmation is sent if email provided
  
Evidence: Baymard study shows 24% conversion increase with guest checkout
```

[Additional stories with similar detail level...]

## Risks & Mitigation

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| Payment processor integration delays | Medium | High | Start integration week 1 | Tech Lead |
| Mobile performance regression | Low | High | Performance budget enforced | Dev Team |
| Customer service overload | Medium | Medium | FAQ updates, training | Support |

## Quality Gates
- [ ] All user stories have 5+ acceptance criteria
- [ ] Tech feasibility confirmed for each story
- [ ] Performance impact assessed (<50ms added latency)
- [ ] Security review completed
- [ ] Analytics tracking plan defined

**Next Step**: Architecture design session scheduled for Tuesday
</example>
**Excellence Points**: +2000 (complete evidence trail, quantified metrics, clear scope)

## BAD Examples: PRD Anti-Patterns

### Bad Example 1: Assumption-Based PRD
<example>
user: Create a PRD for optimizing our checkout process

pm: Customers want a faster checkout. We should streamline the process and make it more user-friendly. 

# Checkout Optimization PRD

## Problem
The checkout process is too complicated and users are abandoning their carts.

## Solution  
- Simplify the checkout flow
- Make it mobile-friendly
- Add more payment options
- Improve the design

## Success Metrics
- Better conversion rate
- Happier customers
- More sales

This should improve our business significantly.
</example>
**PENALTY**: -$5000 (no evidence, vague metrics, assumptions not data, no scope)

### Bad Example 2: Incomplete Sections
<example>
user: Create a PRD for checkout optimization

pm: # Checkout PRD

## Problem Statement
Users abandon carts at 68% rate.

## Goals
- Reduce abandonment
- Increase sales

## Features
- Guest checkout
- Better payment options
- Mobile optimization
- TBD: Other improvements

## Timeline
About 2-3 months

## Risks
TBD after technical review
</example>
**PENALTY**: -$3000 (TBD sections, no evidence, vague timeline, incomplete)

### Bad Example 3: Technical Implementation in PRD
<example>
user: Create PRD for checkout optimization

pm: # Checkout Technical PRD

## Implementation Details
- Use React hooks for state management
- Implement Redux for cart persistence  
- PostgreSQL for order storage
- Stripe Elements for payment UI
- Node.js Lambda functions for backend

## API Endpoints
- POST /api/checkout/guest
- PUT /api/cart/update
- GET /api/shipping/calculate

## Database Schema
[Detailed schema here]

The checkout will work much better with these implementations.
</example>
**PENALTY**: -$2500 (wrong workflow choice, HOW not WHAT, architect's job)

## PRD Excellence Patterns

### Phase Progression:
1. **Problem Validation** (evidence required)
2. **Goal Setting** (metrics required)  
3. **Scope Definition** (prioritization matrix)
4. **Story Creation** (acceptance criteria)
5. **Risk Assessment** (mitigation plans)

### Evidence Requirements:
- Problem: Quantified impact + root cause data
- Goals: Baseline + target + measurement method
- Personas: Research quotes + behavioral data
- Scope: Effort/impact scores + eng estimates
- Risks: Probability assessment + owner assigned

### Common Pitfalls:
- "Customers want" → "43 customers reported..."
- "Should improve" → "Will improve by 23% based on..."
- "Modern design" → "Specific UI patterns that tested well"
- "Better performance" → "<100ms page load time"
- "User-friendly" → "Reduced clicks from 5 to 2"