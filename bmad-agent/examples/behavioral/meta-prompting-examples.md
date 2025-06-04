# Meta-Prompting Examples

## GOOD Examples: Self-Improving Prompt Engineering and Context Optimization

### Example 1: Dynamic Prompt Optimization Based on Task Context
<example>
user: Create a user story for payment processing feature

meta-prompter: [analyzing task context, optimizing prompt strategy, selecting best approach]

## Meta-Prompting Analysis: User Story Creation

### Context Analysis and Prompt Strategy Selection
**Task Classification:**
- **Type:** Product requirement specification
- **Complexity:** Medium (involves business logic, user experience, technical implementation)
- **Stakeholders:** Product Manager, Development Team, QA Team
- **Domain:** E-commerce payment processing
- **Criticality:** High (revenue-impacting feature)

**Historical Performance Analysis:**
```
Previous User Story Tasks (Last 30 days):
├── Simple CRUD stories: 92% stakeholder satisfaction
├── Payment/financial stories: 76% satisfaction (needs improvement)
├── Integration stories: 84% satisfaction
└── UX-focused stories: 89% satisfaction

Pattern Recognition:
- Payment stories require more security considerations
- Financial features need compliance details
- Integration stories need technical specification
- UX stories need interaction details
```

### Meta-Prompt Engineering Strategy
**Selected Approach:** Enhanced Domain-Specific Prompting with Multi-Perspective Analysis

**Optimized Prompt Construction:**
```
Meta-Prompt Layer 1: Domain Context Setting
"Acting as a Product Owner with 5+ years payment processing experience, 
considering PCI compliance, user security concerns, and business revenue impact..."

Meta-Prompt Layer 2: Quality Framework Integration
"Apply INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
with specific attention to payment security and compliance requirements..."

Meta-Prompt Layer 3: Stakeholder Perspective Integration
"Consider viewpoints of:
- End users (security concerns, ease of use)
- Developers (technical implementation, testing complexity)  
- Compliance team (PCI DSS requirements, audit trail)
- Business stakeholders (revenue impact, conversion optimization)"

Meta-Prompt Layer 4: Success Pattern Application
"Based on analysis of 47 successful payment stories, include:
- Clear acceptance criteria with security requirements
- Edge case handling (failed payments, network issues)
- Compliance checkpoints (PCI DSS validation)
- User experience considerations (error messaging, loading states)"
```

### Dynamically Generated User Story
**Result of Optimized Meta-Prompting:**

```
User Story: Secure Credit Card Payment Processing

As a customer completing a purchase
I want to securely enter my credit card information and process payment
So that I can complete my transaction quickly and safely

Acceptance Criteria:
□ Customer can enter credit card details (number, expiry, CVV, name)
□ System validates card format in real-time (client-side)
□ Payment processing completes within 3 seconds (95th percentile)
□ Success confirmation displays transaction ID and receipt option
□ Failed payments show specific, actionable error messages
□ All PCI DSS Level 1 requirements met throughout process

Security Requirements:
□ Card details never stored in application database
□ All payment data encrypted in transit (TLS 1.3)
□ Payment form served over HTTPS with security headers
□ Input validation prevents injection attacks
□ Rate limiting prevents brute force attempts (5 attempts/minute)

Technical Implementation Notes:
□ Integrate with Stripe Payment Intent API for processing
□ Implement client-side card validation using Stripe.js
□ Server-side validation of all payment parameters
□ Idempotency keys prevent duplicate charges
□ Webhook handling for asynchronous payment updates

User Experience Requirements:
□ Loading state during payment processing
□ Progress indicator showing payment steps
□ Clear error messaging without exposing security details
□ Mobile-optimized payment form with large touch targets
□ Accessibility compliance (WCAG 2.1 AA)

Compliance Validation:
□ PCI DSS self-assessment questionnaire completed
□ Security review by compliance team required
□ Penetration testing of payment flow required
□ Documentation of data flow for compliance audit

Definition of Done:
□ Code review completed by senior developer
□ Security review completed by InfoSec team
□ Unit tests covering payment logic (90% coverage)
□ Integration tests for payment scenarios (happy path + errors)
□ Manual testing on 3 different devices/browsers
□ Compliance team sign-off on PCI requirements
□ Performance testing meets 3-second requirement
□ Accessibility testing completed
□ Documentation updated (API docs, runbooks)

Story Points: 8
Dependencies: Stripe account setup, SSL certificate validation
Risks: Payment gateway downtime, compliance review delays
```

### Meta-Prompt Effectiveness Analysis
**Quality Metrics Comparison:**
```
Standard Prompt Result:
- Acceptance criteria: 3 basic items
- Security considerations: 0 mentioned
- Compliance details: 0 mentioned
- Stakeholder satisfaction: 6.2/10

Optimized Meta-Prompt Result:
- Acceptance criteria: 6 comprehensive items + 4 categories
- Security considerations: 5 specific requirements
- Compliance details: 4 validation checkpoints  
- Stakeholder satisfaction: 9.1/10 (projected based on similar stories)
```

### Self-Improving Prompt Pattern
**Meta-Learning Integration:**
```typescript
interface PromptOptimization {
  taskContext: TaskContext;
  historicalPerformance: PerformanceMetrics;
  stakeholderFeedback: FeedbackData;
  domainExpertise: DomainKnowledge;
  qualityFrameworks: QualityStandards;
}

class MetaPrompter {
  optimizePrompt(task: Task): OptimizedPrompt {
    const context = this.analyzeTaskContext(task);
    const patterns = this.findSuccessfulPatterns(context);
    const optimizations = this.applyLearnings(patterns);
    
    return this.constructPrompt(context, optimizations);
  }
  
  learnFromOutcome(task: Task, outcome: TaskOutcome): void {
    this.updatePerformanceMetrics(task.type, outcome.quality);
    this.refineLearningPatterns(task.context, outcome.feedback);
    this.adjustPromptStrategies(outcome.improvements);
  }
}
```

Evidence: Context analysis, historical performance data, stakeholder feedback, quality framework integration
</example>
**Excellence Points**: +2000 (dynamic optimization, measurable improvement, self-learning system)

### Example 2: Adaptive Complexity Management in Technical Discussions
<example>
user: Explain microservices architecture to our team

meta-prompter: [analyzing audience expertise, adapting explanation complexity, optimizing learning outcomes]

## Meta-Prompting Analysis: Technical Explanation Optimization

### Audience Analysis and Complexity Calibration
**Team Expertise Assessment:**
```
Audience Profile Analysis:
├── Senior Developers (2): 8/10 distributed systems knowledge
├── Mid-level Developers (3): 5/10 distributed systems knowledge  
├── Junior Developers (2): 2/10 distributed systems knowledge
├── Product Manager (1): 3/10 technical architecture knowledge
├── Designer (1): 1/10 backend architecture knowledge

Knowledge Distribution:
- Advanced concepts: 22% of audience ready
- Intermediate concepts: 56% of audience ready
- Basic concepts: 100% of audience needs foundation
```

**Historical Learning Pattern Analysis:**
```
Previous Technical Explanations (Last 6 months):
├── High-level overview → 67% comprehension
├── Deep technical dive → 23% comprehension  
├── Progressive disclosure → 89% comprehension
├── Interactive examples → 94% comprehension

Successful Pattern: Start simple, build complexity, use concrete examples
```

### Adaptive Meta-Prompt Strategy
**Selected Approach:** Progressive Disclosure with Interactive Learning

**Meta-Prompt Optimization:**
```
Layer 1: Baseline Understanding Check
"Before explaining microservices, assess team's current mental model of:
- Monolithic applications (what they know)
- API concepts (shared vocabulary)
- Database architecture (current experience)"

Layer 2: Progressive Complexity Introduction  
"Build explanation in 4 levels:
1. Conceptual analogy (accessible to all)
2. Practical benefits (business context)
3. Technical implementation (for developers)
4. Advanced considerations (for seniors)"

Layer 3: Learning Style Adaptation
"Use multiple explanation methods:
- Visual diagrams (for visual learners)
- Code examples (for hands-on learners)
- Real-world analogies (for conceptual learners)
- Interactive discussion (for collaborative learners)"

Layer 4: Validation and Adjustment
"Check understanding at each level before proceeding.
Adjust complexity based on questions and engagement."
```

### Dynamically Adapted Explanation
**Level 1: Conceptual Foundation (Everyone)**
```
Microservices Architecture Explanation

Think of a traditional web application like a restaurant:
- Monolithic app = One huge kitchen doing everything
  * One chef handles orders, cooking, desserts, drinks, billing
  * If the chef gets overwhelmed, the whole restaurant slows down
  * If one thing breaks (oven), everything stops

- Microservices = Specialized stations
  * Order station, grill station, dessert station, drinks station
  * Each station is independent and expert at their job
  * If grill breaks, you can still serve drinks and desserts
  * Each station can scale independently (more bartenders on Friday night)

Key Insight: Break big systems into smaller, specialized, independent services.
```

**Level 2: Business Benefits (PM + Team)**
```
Why Consider Microservices? Business Value

1. Team Scaling
   - Monolith: 8 developers working on same codebase = conflicts
   - Microservices: 3 teams of 3 developers, each owning 2-3 services

2. Technology Flexibility  
   - Monolith: Stuck with original technology choices
   - Microservices: Use best tool for each job (Python for ML, Go for APIs)

3. Deployment Independence
   - Monolith: Bug fix requires full system deployment
   - Microservices: Update payment service without touching user management

4. Fault Isolation
   - Monolith: Billing bug crashes entire application
   - Microservices: Billing issues don't affect product browsing

Our Context: With 12 developers and plans to grow to 25, we're hitting the monolith scaling wall.
```

**Level 3: Technical Implementation (Developers)**
```
Technical Architecture Deep Dive

Current State (Monolith):
┌─────────────────────────────────────┐
│ Single Application                  │
├─────────────────────────────────────┤
│ User Management                     │
│ Product Catalog                     │
│ Shopping Cart                       │
│ Payment Processing                  │
│ Order Management                    │
│ Notifications                       │
└─────────────────────────────────────┘
│
▼
┌─────────────────────────────────────┐
│ Single Database                     │
└─────────────────────────────────────┘

Proposed State (Microservices):
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ User Service│ │Product Svc  │ │Payment Svc  │
├─────────────┤ ├─────────────┤ ├─────────────┤
│ User DB     │ │ Product DB  │ │ Payment DB  │
└─────────────┘ └─────────────┘ └─────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
            ┌─────────────────────────┐
            │ API Gateway             │
            │ (Request Routing)       │
            └─────────────────────────┘

Implementation Approach:
1. Database-per-service (data ownership)
2. API-first communication (no shared databases)
3. Independent deployment pipelines
4. Service discovery and load balancing
```

**Level 4: Advanced Considerations (Senior Developers)**
```
Production-Ready Microservices Challenges

1. Data Consistency
   Challenge: No distributed transactions across services
   Solution: Saga pattern for multi-service workflows
   
   Example: Order Processing Saga
   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
   │Reserve Items│→│Process Pay't│→│Create Order │
   │(Inventory)  │ │(Payment)    │ │(Orders)     │
   └─────────────┘ └─────────────┘ └─────────────┘
   
   If payment fails: Auto-release inventory reservation

2. Network Latency & Failures
   Challenge: Service A calls Service B calls Service C = 150ms+ latency
   Solutions:
   - Async messaging where possible
   - Circuit breaker pattern for failures
   - Request/response caching
   
3. Operational Complexity
   Challenge: 8 services = 8 deployment pipelines, monitoring, logging
   Requirements:
   - Container orchestration (Kubernetes)
   - Centralized logging (ELK stack)
   - Distributed tracing (Jaeger)
   - Service mesh (Istio) for advanced networking

4. Team Boundaries
   Challenge: Conway's Law - architecture reflects team structure
   Strategy: Align service boundaries with team responsibilities
   
   Example Team Structure:
   - User Experience Team → User Service + Frontend
   - Commerce Team → Product + Cart + Order Services  
   - Platform Team → Payment + Notification Services
```

### Real-Time Complexity Adjustment
**Audience Engagement Monitoring:**
```
During Explanation - Adaptive Responses:

If questions about Level 1 concepts:
→ Slow down, use more analogies, check understanding

If advanced questions during Level 2:
→ "Great question - let's explore that in Level 3"

If confusion signals (blank stares, no questions):
→ Pause, ask for understanding check, provide examples

If engagement high + advanced questions:
→ Accelerate to deeper technical details
```

### Meta-Learning Feedback Loop
**Post-Explanation Analysis:**
```
Effectiveness Metrics:
├── Comprehension Check (Quiz/Discussion): 87% accuracy
├── Follow-up Questions Quality: High-level architectural questions
├── Team Confidence in Topic: 7.8/10 (up from 3.2/10)
├── Implementation Readiness: 6/9 team members feel ready for next steps

Learning Pattern Updates:
├── Progressive disclosure confirmed effective for mixed audiences
├── Visual diagrams crucial for complex technical concepts
├── Real-world analogies bridge knowledge gaps effectively
├── Interactive validation prevents losing audience
```

### Self-Optimizing Explanation Framework
```typescript
class AdaptiveExplainer {
  explainTopic(topic: string, audience: Audience): Explanation {
    const complexity = this.assessAudienceReadiness(audience);
    const strategy = this.selectOptimalStrategy(topic, complexity);
    const levels = this.createProgressiveLevels(topic, strategy);
    
    return this.executeAdaptiveExplanation(levels, audience);
  }
  
  monitorComprehension(audience: Audience): ComprehensionMetrics {
    return {
      engagementLevel: this.detectEngagement(),
      questionQuality: this.analyzeQuestions(),
      confusionSignals: this.detectConfusion(),
      readinessForNext: this.assessProgression()
    };
  }
  
  adaptInRealTime(metrics: ComprehensionMetrics): ExplanationAdjustment {
    if (metrics.confusionSignals.high) {
      return { action: 'simplify', addAnalogies: true };
    }
    if (metrics.questionQuality.advanced) {
      return { action: 'accelerate', addDepth: true };
    }
    return { action: 'continue', currentPace: true };
  }
}
```

Evidence: Audience analysis, complexity calibration, progressive disclosure, real-time adaptation, effectiveness measurement
</example>
**Excellence Points**: +1900 (adaptive complexity, audience analysis, real-time adjustment, progressive learning)

### Example 3: Context-Aware Quality Standard Enforcement
<example>
user: Review this pull request for our critical payment processing system

meta-prompter: [analyzing context criticality, adjusting quality standards, optimizing review approach]

## Meta-Prompting Analysis: Critical System Code Review

### Context Criticality Assessment
**System Classification:**
```
Code Review Context Analysis:
├── System: Payment Processing (Critical)
├── Component: Credit Card Transaction Handler
├── Business Impact: High (revenue-affecting, PCI compliance)
├── User Impact: Critical (payment failures = lost sales)
├── Security Level: Maximum (PCI DSS Level 1 required)
├── Change Type: Bug fix (production issue)
├── Timeline: Urgent (affecting live customers)
```

**Risk Profile Calculation:**
```
Risk Factors Assessment:
├── Financial Impact: $50K/hour if payments fail
├── Compliance Risk: PCI violations = $500K+ fines
├── Customer Impact: 1,200 active users affected
├── Reputation Risk: Payment security incidents = brand damage
├── Technical Risk: Change in core transaction logic

Overall Risk Level: CRITICAL
Required Review Depth: Maximum
Quality Standards: Zero-tolerance for defects
```

### Dynamic Quality Standard Calibration
**Standard Review vs Critical System Review:**
```
Standard Code Review Requirements:
├── Functionality: Does it work?
├── Code quality: Is it readable?
├── Tests: Are there tests?
├── Performance: Is it reasonably fast?

Critical Payment System Review (Enhanced Standards):
├── Security: Threat model analysis required
├── Compliance: PCI DSS checklist validation
├── Error Handling: Every possible failure scenario covered
├── Performance: Sub-100ms response time verified
├── Testing: 99%+ coverage including edge cases
├── Monitoring: Comprehensive observability
├── Rollback: Immediate rollback capability
├── Documentation: Security and compliance docs
```

### Meta-Prompt Optimization for Critical Review
**Enhanced Review Strategy:**
```
Meta-Prompt Layer 1: Context Sensitivity
"Reviewing critical payment processing code requiring:
- Zero defect tolerance (financial and compliance impact)
- Security-first analysis (PCI compliance mandatory)
- Performance validation (revenue impact of latency)
- Comprehensive testing verification (production failure prevention)"

Meta-Prompt Layer 2: Review Methodology
"Apply STRIDE threat modeling:
- Spoofing: Authentication vulnerabilities
- Tampering: Data integrity issues  
- Repudiation: Audit trail gaps
- Information Disclosure: Data exposure risks
- Denial of Service: Performance vulnerabilities
- Elevation of Privilege: Authorization flaws"

Meta-Prompt Layer 3: Quality Gates
"Enforce critical system quality gates:
- Security review (InfoSec team required)
- Performance testing (load testing mandatory)
- Compliance validation (PCI checklist complete)
- Error scenario testing (chaos engineering)
- Monitoring verification (alerting and dashboards)"

Meta-Prompt Layer 4: Decision Framework
"Approval criteria for critical payment code:
- Zero critical security issues
- All performance SLAs met
- 99%+ test coverage achieved
- Compliance requirements verified
- Rollback strategy tested and documented"
```

### Comprehensive Critical System Review
**Code Analysis Results:**
```typescript
// PULL REQUEST REVIEW: Payment Transaction Handler Bug Fix
// File: PaymentProcessor.ts (Lines 45-78)

🔴 CRITICAL SECURITY ISSUE DETECTED
Line 67: Credit card number logged in error handling
```typescript
catch (error) {
  logger.error('Payment failed', { 
    cardNumber: request.cardNumber,  // ❌ PCI VIOLATION
    error: error.message 
  });
}
```
**Violation:** PCI DSS Requirement 3.3 - Mask PAN when displayed
**Impact:** Critical compliance violation, potential $500K+ fine
**Fix Required:** Remove PAN from logs immediately
```typescript
// CORRECTED VERSION
catch (error) {
  logger.error('Payment failed', { 
    cardLast4: request.cardNumber.slice(-4),  // ✅ PCI COMPLIANT
    transactionId: request.transactionId,
    error: error.message 
  });
}
```

🔴 CRITICAL PERFORMANCE ISSUE
Line 52: Synchronous database call in payment flow
```typescript
const user = await db.query('SELECT * FROM users WHERE id = ?', [userId]);
```
**Issue:** Blocking database call adds 45ms average latency
**Impact:** Payment timeout risk, poor user experience
**SLA Violation:** Target <100ms, current path = 145ms average
**Fix Required:** Use async pattern with connection pooling

🟡 ERROR HANDLING GAP
Lines 45-50: Insufficient error categorization
```typescript
if (!response.success) {
  throw new Error('Payment failed');  // ❌ Generic error
}
```
**Issue:** Generic error prevents proper user messaging and debugging
**Impact:** Poor customer experience, difficult troubleshooting
**Fix Required:** Categorized error types with user-friendly messages

### Security Threat Model Analysis
**STRIDE Analysis Results:**
```
Spoofing Threats:
├── Authentication: ✅ JWT validation present
├── Service identity: ⚠️ No mutual TLS verification
├── Request origin: ✅ Origin validation implemented

Tampering Threats:  
├── Request integrity: ✅ Request signing implemented
├── Data in transit: ✅ TLS 1.3 encryption
├── Data at rest: ❌ Card data should not be stored (violation found)

Repudiation Threats:
├── Audit logging: ⚠️ Missing user action correlation
├── Transaction trail: ✅ Complete transaction logging
├── Non-repudiation: ✅ Digital signatures present

Information Disclosure:
├── Data exposure: ❌ PCI data in logs (critical issue)
├── Error messages: ⚠️ Too detailed error responses
├── Access controls: ✅ Proper authorization checks

Denial of Service:
├── Rate limiting: ✅ Implemented per user/IP
├── Resource exhaustion: ⚠️ No circuit breaker pattern
├── Input validation: ✅ Comprehensive validation

Elevation of Privilege:
├── Authorization: ✅ Role-based access control
├── Privilege escalation: ✅ No admin shortcuts found
├── Service permissions: ✅ Least privilege principle
```

### Performance and Reliability Analysis
**Performance Testing Results:**
```
Load Testing (Critical System Requirements):
├── Target: <100ms p95 response time
├── Current: 145ms p95 (FAILS requirement)
├── Bottleneck: Database query (45ms) + API calls (78ms)
├── Recommendation: Connection pooling + async optimization

Reliability Testing:
├── Error rate: 0.02% (MEETS <0.1% requirement)
├── Availability: 99.97% (MEETS >99.95% requirement)  
├── Failover time: 12 seconds (EXCEEDS <10s requirement)

Scalability Testing:
├── Concurrent users: 500 (meets 1000 target under optimization)
├── Throughput: 850 TPS (meets 1000 TPS target)
├── Memory usage: Stable under load ✅
```

### Compliance Validation Checklist
**PCI DSS Compliance Review:**
```
Requirements Validation:
├── Req 1: Firewall configuration ✅
├── Req 2: Default passwords changed ✅  
├── Req 3: Protect stored cardholder data ❌ (logging violation)
├── Req 4: Encrypt transmission ✅
├── Req 5: Antivirus software ✅
├── Req 6: Secure systems/applications ⚠️ (needs security review)
├── Req 7: Restrict access by business need ✅
├── Req 8: Identify and authenticate access ✅
├── Req 9: Restrict physical access ✅
├── Req 10: Track network access ⚠️ (incomplete audit logging)
├── Req 11: Regular security testing ⚠️ (schedule needed)
├── Req 12: Information security policy ✅

Compliance Status: FAILS (critical violations must be fixed)
```

### Testing Coverage Analysis
**Critical System Testing Requirements:**
```
Current Test Coverage Analysis:
├── Unit Tests: 87% coverage (TARGET: 99%+ for critical systems)
├── Integration Tests: 45% scenarios (TARGET: 95%+ coverage)
├── Security Tests: 23% attack vectors (TARGET: 100% coverage)
├── Performance Tests: Basic load testing (MISSING: chaos engineering)
├── Compliance Tests: None (REQUIRED: PCI validation tests)

Missing Critical Test Scenarios:
├── Card number validation edge cases
├── Payment gateway timeout handling
├── Concurrent transaction processing
├── Network partition scenarios  
├── Database connection failures
├── Memory pressure conditions
├── PCI compliance automated validation
```

### Critical System Review Decision
**REVIEW STATUS: REJECTED - CRITICAL ISSUES FOUND**

**Blocking Issues (Must Fix Before Re-Review):**
1. **PCI Compliance Violation:** Remove card number from error logs
2. **Performance SLA Violation:** Optimize database queries to meet <100ms target  
3. **Testing Coverage Gap:** Achieve 99%+ test coverage for critical paths
4. **Security Review Missing:** InfoSec team review required before approval

**Non-Blocking Recommendations:**
1. Implement circuit breaker pattern for resilience
2. Add comprehensive audit logging correlation
3. Enhance error categorization for better UX
4. Schedule penetration testing for payment flow

**Required Actions Before Re-Submission:**
- [ ] Fix PCI logging violation (Security team verification required)
- [ ] Performance optimization with load testing proof
- [ ] Complete test coverage for critical payment paths  
- [ ] Security team review and sign-off
- [ ] Compliance team PCI validation
- [ ] Chaos engineering test execution

**Estimated Time to Address:** 3-5 days
**Re-review Required:** Yes, with security and compliance team participation

### Meta-Learning from Critical Review
**Quality Standard Effectiveness:**
```
Standard Review vs Critical Review Outcomes:
├── Standard: Would have missed PCI violation (25% chance of detection)
├── Critical: Detected all compliance issues (100% detection rate)
├── Standard: Performance issue likely missed (40% detection rate)
├── Critical: Performance SLA verification caught violation (100% detection)

Enhanced Standards ROI:
├── Cost: 3x review time (45 minutes vs 15 minutes)
├── Benefit: Prevented potential $500K+ compliance violation
├── Quality: Zero critical defects reach production
├── Confidence: 95% confidence in production readiness
```

Evidence: Context criticality assessment, enhanced quality standards, security threat modeling, compliance validation, comprehensive testing analysis
</example>
**Excellence Points**: +2400 (critical system analysis, comprehensive quality standards, compliance validation, risk assessment)

## BAD Examples: Meta-Prompting Anti-Patterns

### Bad Example 1: One-Size-Fits-All Prompting
<example>
user: Create a user story for payment processing feature

meta-prompter: I'll create a user story using our standard template. 

As a user, I want to process payments so that I can complete transactions. The story should have acceptance criteria and be testable.
</example>
**PENALTY**: -$2000 (no context analysis, generic approach, missing domain expertise)

### Bad Example 2: Static Complexity Management
<example>
user: Explain microservices architecture to our team

meta-prompter: Microservices is a complex topic. I'll give you the standard explanation about breaking monoliths into smaller services.

This is how most companies implement microservices architecture...
</example>
**PENALTY**: -$1800 (no audience analysis, static approach, missing adaptation)

## Key Patterns for Meta-Prompting Excellence

### Meta-Prompting Framework:
1. **Context Analysis**: Deep understanding of task, audience, and constraints
2. **Strategy Selection**: Choose optimal approach based on context
3. **Dynamic Adaptation**: Real-time adjustment based on feedback
4. **Quality Optimization**: Enhanced standards for critical contexts
5. **Self-Learning**: Continuous improvement based on outcomes

### Meta-Prompt Optimization:
1. **Multi-Layer Prompting**: Context, strategy, execution, validation layers
2. **Audience Calibration**: Adapt complexity and style to audience expertise
3. **Domain Expertise**: Apply specialized knowledge for domain-specific tasks
4. **Quality Standards**: Adjust quality requirements based on criticality
5. **Feedback Integration**: Use historical performance to improve prompts

### Adaptive Strategies:
1. **Progressive Disclosure**: Build complexity gradually based on comprehension
2. **Context Sensitivity**: Adjust approach based on task criticality and impact
3. **Real-Time Monitoring**: Track engagement and adjust accordingly
4. **Multiple Modalities**: Use visual, verbal, and interactive explanations
5. **Validation Loops**: Check understanding before proceeding

### Never Do in Meta-Prompting:
- Use same approach regardless of context or audience
- Ignore historical performance data and feedback
- Skip audience analysis and expertise assessment
- Apply static quality standards regardless of criticality
- Miss opportunities for real-time adaptation and improvement

### Memory Integration Pattern:
Before meta-prompting: "What context patterns and strategies have worked best for similar tasks?"
After execution: "What meta-prompting approaches and outcomes should we remember for optimization?"