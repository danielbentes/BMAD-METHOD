# Requirements Gathering Excellence Examples

## GOOD Examples: Systematic Requirements Discovery and Validation

### Example 1: Customer-Centric Requirements Discovery
<example>
user: Gather requirements for a new customer onboarding system

requirements-analyst: [applying systematic requirements discovery with customer validation and stakeholder alignment]

## Customer Onboarding System Requirements Discovery

### Requirements Discovery Framework
**Stakeholder Identification and Analysis:**
```
Primary Stakeholders:
├── New Customers: Users of the onboarding system
├── Customer Success Team: Manages onboarding process
├── Sales Team: Handoff customers to onboarding
├── Support Team: Handles onboarding issues
├── Engineering Team: Implements the system
├── Product Manager: Owns customer experience strategy

Secondary Stakeholders:
├── Executive Team: Business impact and ROI
├── Legal Team: Compliance and data privacy
├── Marketing Team: Customer acquisition integration
├── Operations Team: System maintenance and scaling
```

**Current State Analysis:**
```
Existing Onboarding Process Assessment:
├── Process Duration: 14-21 days average (industry benchmark: 7-10 days)
├── Completion Rate: 67% (33% of customers never complete onboarding)
├── Customer Satisfaction: 6.2/10 (below 8.0 target)
├── Resource Intensity: 12 hours customer success time per customer
├── Pain Points: Manual handoffs, duplicate data entry, unclear progress

Quantified Business Impact:
├── Lost Revenue: $340K annually from incomplete onboarding
├── Support Costs: $89K annually from onboarding confusion
├── Customer Success Overhead: 720 hours monthly on manual tasks
├── Customer Churn: 23% higher in first 90 days vs industry average
```

### Customer Research and Discovery
**Direct Customer Research:**
```
Customer Interview Program (n=24 customers across segments):
├── Recent Customers (0-3 months): 8 interviews
├── Established Customers (6-12 months): 8 interviews
├── Churned Customers (exit interviews): 8 interviews

Interview Methodology:
├── Semi-structured interviews (45 minutes each)
├── Journey mapping exercises
├── Pain point prioritization
├── Feature importance ranking
├── Competitive experience comparison

Key Customer Insights:
├── Onboarding Clarity: 78% report unclear next steps
├── Progress Visibility: 89% want better progress tracking
├── Time Investment: 67% feel onboarding takes too long
├── Value Realization: 45% unclear on product value during onboarding
├── Support Access: 72% had difficulty getting help when stuck
```

**Customer Journey Analysis:**
```
Current Onboarding Journey Map:

Phase 1: Welcome and Setup (Days 1-3)
├── Customer Actions: Account creation, initial configuration
├── Pain Points: Complex setup process, too many decisions upfront
├── Emotional State: Excited but overwhelmed
├── Success Rate: 89% complete this phase

Phase 2: Configuration and Integration (Days 4-10)
├── Customer Actions: Connect data sources, configure settings
├── Pain Points: Technical complexity, unclear instructions
├── Emotional State: Frustrated, considering alternatives
├── Success Rate: 76% complete this phase

Phase 3: Training and Adoption (Days 11-21)
├── Customer Actions: Learn features, invite team members
├── Pain Points: Training materials unclear, no guided practice
├── Emotional State: Cautiously optimistic or resigned
├── Success Rate: 67% complete this phase

Ideal Future Journey Map:

Phase 1: Personalized Welcome (Days 1-2)
├── Customer Actions: Profile-based setup, guided configuration
├── Improvement Goals: Reduce setup complexity, personalize experience
├── Success Criteria: 95% completion rate, 8+ satisfaction

Phase 2: Value-First Integration (Days 3-5)
├── Customer Actions: Quick wins, gradual complexity increase
├── Improvement Goals: Show value early, progressive disclosure
├── Success Criteria: 90% completion rate, clear progress tracking

Phase 3: Mastery and Expansion (Days 6-7)
├── Customer Actions: Advanced features, team collaboration
├── Improvement Goals: Self-service learning, peer connections
├── Success Criteria: 85% completion rate, referral generation
```

### Functional Requirements Definition
**Core System Requirements:**
```
User Management and Authentication:
├── REQ-001: Single sign-on integration with existing systems
├── REQ-002: Role-based access control (admin, user, viewer)
├── REQ-003: User profile management with progress tracking
├── REQ-004: Team invitation and collaboration features
├── REQ-005: Session management and security controls

Onboarding Flow Management:
├── REQ-006: Personalized onboarding paths based on customer profile
├── REQ-007: Progress tracking with visual indicators
├── REQ-008: Step completion validation and prerequisites
├── REQ-009: Dynamic content based on customer selections
├── REQ-010: Pause and resume functionality

Integration and Data Management:
├── REQ-011: CRM integration for customer data synchronization
├── REQ-012: Email automation for onboarding communications
├── REQ-013: Analytics tracking for completion and engagement metrics
├── REQ-014: Document management for onboarding materials
├── REQ-015: API access for third-party integrations

Communication and Support:
├── REQ-016: In-app messaging for customer success communication
├── REQ-017: Help documentation contextual to onboarding steps
├── REQ-018: Video tutorials embedded in onboarding flow
├── REQ-019: Live chat integration for immediate support
├── REQ-020: Feedback collection at each onboarding stage
```

**Non-Functional Requirements:**
```
Performance Requirements:
├── NFR-001: Page load times <2 seconds for all onboarding screens
├── NFR-002: Support 500 concurrent users without degradation
├── NFR-003: 99.9% uptime during business hours
├── NFR-004: Mobile responsive design for all onboarding flows
├── NFR-005: Offline capability for essential onboarding content

Security and Compliance Requirements:
├── NFR-006: SOC2 Type II compliance for data handling
├── NFR-007: GDPR compliance for EU customer data
├── NFR-008: Data encryption in transit and at rest
├── NFR-009: Audit trail for all onboarding activities
├── NFR-010: Role-based data access controls

Usability Requirements:
├── NFR-011: WCAG 2.1 AA accessibility compliance
├── NFR-012: Multi-language support (English, Spanish, French)
├── NFR-013: Browser compatibility (Chrome, Firefox, Safari, Edge)
├── NFR-014: Maximum 3 clicks to reach any onboarding function
├── NFR-015: Self-explanatory interface requiring minimal training

Scalability Requirements:
├── NFR-016: Support 10x current customer volume without architecture changes
├── NFR-017: Horizontal scaling capability for peak usage periods
├── NFR-018: Database partitioning strategy for large customer datasets
├── NFR-019: CDN integration for global content delivery
├── NFR-020: Auto-scaling infrastructure based on demand
```

### Business Rules and Validation
**Business Logic Requirements:**
```
Onboarding Flow Rules:
├── BR-001: Customer type determines onboarding path (Enterprise, SMB, Individual)
├── BR-002: Prerequisites must be completed before advancing to next step
├── BR-003: Onboarding can be paused for maximum 30 days before expiration
├── BR-004: Customer success intervention triggered if stuck >48 hours
├── BR-005: Completion certificate generated upon successful onboarding

Data Validation Rules:
├── BR-006: All customer profile fields validated against predefined formats
├── BR-007: Integration credentials tested before proceeding to next step
├── BR-008: Duplicate account detection and merge procedures
├── BR-009: Data quality checks with automated correction suggestions
├── BR-010: Compliance verification for regulated industry customers

Communication Rules:
├── BR-011: Automated emails sent based on progress and time triggers
├── BR-012: Customer success assignment based on customer value and complexity
├── BR-013: Escalation procedures for customers falling behind schedule
├── BR-014: Feedback requests sent at completion milestones
├── BR-015: Reference customer identification and referral program integration
```

### Requirements Validation and Prioritization
**Stakeholder Validation Process:**
```
Requirements Review Sessions:
├── Customer Validation: 12 customers reviewed detailed requirements
├── Internal Stakeholder Review: All stakeholder groups provided input
├── Technical Feasibility: Engineering team validated implementation approach
├── Business Impact Assessment: Product and executive team approved priorities

Validation Results:
├── Customer Agreement: 94% of requirements validated by customer interviews
├── Technical Feasibility: 100% of requirements technically achievable
├── Business Value: Requirements prioritized by customer impact and business value
├── Timeline Compatibility: All requirements achievable within 16-week timeline

Requirements Prioritization (MoSCoW Method):
├── Must Have (Launch Blockers): REQ-001 through REQ-015, NFR-001 through NFR-010
├── Should Have (High Value): REQ-016 through REQ-020, NFR-011 through NFR-015
├── Could Have (Nice to Have): Additional integrations, advanced analytics
├── Won't Have (Future Releases): AI-powered recommendations, gamification
```

**Success Criteria Definition:**
```
Measurable Success Metrics:
├── Onboarding Completion Rate: Increase from 67% to 85%
├── Time to Value: Reduce from 14-21 days to 7 days
├── Customer Satisfaction: Increase from 6.2/10 to 8.5/10
├── Customer Success Efficiency: Reduce manual effort from 12 to 4 hours per customer
├── Customer Retention: Increase 90-day retention by 15%

Acceptance Criteria:
├── All functional requirements implemented and tested
├── Performance benchmarks met under load testing
├── Security audit passed with no critical vulnerabilities
├── User acceptance testing completed with 90% satisfaction
├── Integration testing validated with all third-party systems

Launch Readiness Criteria:
├── Customer success team trained on new system
├── Migration plan executed for existing onboarding customers
├── Support documentation complete and accessible
├── Monitoring and alerting systems operational
├── Rollback procedures tested and validated
```

### Requirements Documentation and Management
**Living Requirements Documentation:**
```
Requirements Artifact Organization:
├── Executive Summary: Business case and high-level requirements
├── Functional Specifications: Detailed feature requirements with acceptance criteria
├── Technical Specifications: System architecture and integration requirements
├── User Stories: Customer-focused requirements with business value
├── Data Requirements: Data model, migration, and integration specifications

Documentation Standards:
├── Requirement ID: Unique identifier for traceability
├── Priority: MoSCoW classification with business justification
├── Acceptance Criteria: Testable conditions for completion
├── Dependencies: Prerequisites and related requirements
├── Source: Customer interview, stakeholder input, or business analysis

Change Management Process:
├── Change Request Form: Standardized impact assessment template
├── Approval Authority: Product manager for scope, engineering for technical
├── Impact Analysis: Timeline, budget, and resource implications
├── Stakeholder Communication: Change notification and rationale
├── Version Control: Requirements history and audit trail

Traceability Matrix:
├── Business Objective → Functional Requirement → Design Specification
├── Customer Need → User Story → Acceptance Criteria → Test Case
├── Compliance Requirement → Security Control → Implementation Verification
├── Performance Goal → Non-Functional Requirement → Load Test Validation
```

Evidence: Systematic stakeholder analysis, customer research, requirements validation, prioritization methodology, comprehensive documentation
</example>
**Excellence Points**: +2300 (comprehensive stakeholder analysis, customer research, systematic validation, clear prioritization)

### Example 2: Technical Requirements Analysis with Architecture Alignment
<example>
user: Define technical requirements for a high-performance API gateway system

requirements-analyst: [conducting technical requirements analysis with performance, scalability, and architecture considerations]

## API Gateway Technical Requirements Analysis

### Technical Context and Architecture Analysis
**Current System Assessment:**
```
Existing API Infrastructure:
├── Request Volume: 50M requests/day (peak: 3,000 requests/second)
├── Response Time: P95: 450ms, P99: 1.2s (target: P95 <200ms, P99 <500ms)
├── Availability: 99.2% (target: 99.9%)
├── Error Rate: 2.3% (target: <0.5%)
├── Architecture: Direct service calls, no centralized gateway

Current Pain Points:
├── Service Discovery: Manual configuration, frequent downtime during updates
├── Authentication: Inconsistent implementation across 23 microservices
├── Rate Limiting: Service-level implementation, inconsistent policies
├── Monitoring: Limited visibility into cross-service communication
├── Security: No centralized security policy enforcement
```

**Technical Requirements Discovery:**
```
Architecture Requirements Analysis:
├── Scalability: Support 10x current load (30,000 requests/second)
├── Performance: <50ms additional latency from gateway
├── Availability: 99.99% uptime with multi-region deployment
├── Security: Centralized authentication, authorization, and threat protection
├── Observability: Comprehensive logging, metrics, and distributed tracing

Technology Stack Evaluation:
├── Gateway Options: Kong, Istio, AWS API Gateway, Nginx Plus, Envoy
├── Data Store: Redis Cluster for caching, PostgreSQL for configuration
├── Monitoring: Prometheus/Grafana, Jaeger for distributed tracing
├── Infrastructure: Kubernetes for orchestration, multi-cloud deployment
├── CI/CD: GitOps deployment with automated testing and rollback
```

### Performance and Scalability Requirements
**Quantified Performance Specifications:**
```
Throughput Requirements:
├── REQ-PERF-001: Handle 30,000 requests/second sustained load
├── REQ-PERF-002: Scale to 50,000 requests/second during peak events
├── REQ-PERF-003: Process batch requests up to 1000 operations/request
├── REQ-PERF-004: Support WebSocket connections for real-time features
├── REQ-PERF-005: Handle file uploads up to 100MB through gateway

Latency Requirements:
├── REQ-PERF-006: Add <10ms latency for simple routing operations
├── REQ-PERF-007: Authentication/authorization overhead <20ms
├── REQ-PERF-008: Rate limiting checks complete in <5ms
├── REQ-PERF-009: Request transformation operations <15ms
├── REQ-PERF-010: Health check responses within 1ms

Resource Utilization Requirements:
├── REQ-PERF-011: CPU utilization <70% under normal load
├── REQ-PERF-012: Memory usage <4GB per gateway instance
├── REQ-PERF-013: Network bandwidth efficiency >95%
├── REQ-PERF-014: Disk I/O minimized through caching strategies
├── REQ-PERF-015: Auto-scaling response time <30 seconds

Scalability Requirements:
├── REQ-SCALE-001: Horizontal scaling from 3 to 50 instances
├── REQ-SCALE-002: Zero-downtime scaling operations
├── REQ-SCALE-003: Multi-region deployment with traffic distribution
├── REQ-SCALE-004: Database connection pooling for 1000+ connections
├── REQ-SCALE-005: Cache invalidation across distributed instances
```

### Security and Compliance Requirements
**Comprehensive Security Framework:**
```
Authentication and Authorization:
├── REQ-SEC-001: OAuth 2.0 and OpenID Connect support
├── REQ-SEC-002: JWT token validation with key rotation
├── REQ-SEC-003: API key management with usage tracking
├── REQ-SEC-004: Role-based access control (RBAC) implementation
├── REQ-SEC-005: Multi-factor authentication for admin operations

Threat Protection:
├── REQ-SEC-006: DDoS protection with rate limiting and traffic shaping
├── REQ-SEC-007: SQL injection and XSS attack prevention
├── REQ-SEC-008: Malicious payload detection and blocking
├── REQ-SEC-009: IP allowlisting and denylisting capabilities
├── REQ-SEC-010: Bot detection and automated threat response

Data Protection:
├── REQ-SEC-011: TLS 1.3 encryption for all communications
├── REQ-SEC-012: Sensitive data masking in logs and monitoring
├── REQ-SEC-013: PII detection and redaction capabilities
├── REQ-SEC-014: Audit logging for all security-related events
├── REQ-SEC-015: Compliance with SOC2, GDPR, and HIPAA requirements

Security Monitoring:
├── REQ-SEC-016: Real-time security event detection and alerting
├── REQ-SEC-017: Integration with SIEM systems for threat analysis
├── REQ-SEC-018: Anomaly detection for unusual traffic patterns
├── REQ-SEC-019: Security dashboard with risk metrics
├── REQ-SEC-020: Incident response automation for critical threats
```

### Integration and Operational Requirements
**System Integration Specifications:**
```
Service Integration:
├── REQ-INT-001: Service discovery integration with Kubernetes DNS
├── REQ-INT-002: Load balancing with health check integration
├── REQ-INT-003: Circuit breaker pattern for downstream service protection
├── REQ-INT-004: Request/response transformation and mediation
├── REQ-INT-005: Protocol translation (HTTP, gRPC, WebSocket)

External System Integration:
├── REQ-INT-006: Identity provider integration (Active Directory, Okta)
├── REQ-INT-007: Monitoring system integration (Prometheus, DataDog)
├── REQ-INT-008: Logging aggregation (ELK stack, Splunk)
├── REQ-INT-009: Configuration management (Consul, etcd)
├── REQ-INT-010: Certificate management with automatic renewal

Operational Requirements:
├── REQ-OPS-001: Zero-downtime deployment with blue-green strategy
├── REQ-OPS-002: Configuration changes without service restart
├── REQ-OPS-003: A/B testing capabilities for API version management
├── REQ-OPS-004: Canary deployment support for gradual rollouts
├── REQ-OPS-005: Automatic rollback on health check failures

Development and Testing:
├── REQ-DEV-001: Local development environment with Docker
├── REQ-DEV-002: API testing framework integration
├── REQ-DEV-003: Performance testing automation with load generation
├── REQ-DEV-004: Security testing integration in CI/CD pipeline
├── REQ-DEV-005: Configuration validation and syntax checking
```

### Monitoring and Observability Requirements
**Comprehensive Monitoring Framework:**
```
Metrics and Monitoring:
├── REQ-MON-001: Request/response metrics (count, latency, errors)
├── REQ-MON-002: Throughput monitoring with percentile breakdowns
├── REQ-MON-003: Error rate tracking with categorization
├── REQ-MON-004: Resource utilization monitoring (CPU, memory, network)
├── REQ-MON-005: Business metrics (API usage by customer, feature adoption)

Logging Requirements:
├── REQ-LOG-001: Structured JSON logging for all requests
├── REQ-LOG-002: Correlation ID propagation across services
├── REQ-LOG-003: Configurable log levels without service restart
├── REQ-LOG-004: Log retention policies based on compliance requirements
├── REQ-LOG-005: Real-time log streaming to aggregation systems

Distributed Tracing:
├── REQ-TRACE-001: Request tracing across all microservices
├── REQ-TRACE-002: Performance bottleneck identification
├── REQ-TRACE-003: Error propagation tracking and root cause analysis
├── REQ-TRACE-004: Sampling strategies for high-volume tracing
├── REQ-TRACE-005: Integration with APM tools for service mapping

Alerting and Notification:
├── REQ-ALERT-001: Real-time alerting for SLA violations
├── REQ-ALERT-002: Escalation procedures for critical issues
├── REQ-ALERT-003: Alert correlation to reduce notification noise
├── REQ-ALERT-004: Integration with on-call systems (PagerDuty)
├── REQ-ALERT-005: Automated incident creation for critical alerts
```

### Requirements Validation and Testing
**Technical Validation Framework:**
```
Performance Testing Requirements:
├── Load Testing: Sustained 30,000 RPS for 4 hours
├── Stress Testing: Peak load of 50,000 RPS for 30 minutes
├── Spike Testing: 10x traffic spike handling within 30 seconds
├── Volume Testing: 24-hour continuous operation validation
├── Endurance Testing: 72-hour stability under normal load

Security Testing Requirements:
├── Penetration Testing: Third-party security assessment
├── Vulnerability Scanning: Automated security scanning in CI/CD
├── Authentication Testing: Token validation and session management
├── Authorization Testing: Access control verification
├── Input Validation Testing: Malicious payload injection testing

Integration Testing Requirements:
├── Service Discovery: Dynamic service registration and discovery
├── Health Check Integration: Automatic failover testing
├── Circuit Breaker Testing: Downstream service failure scenarios
├── Configuration Change Testing: Runtime configuration updates
├── Deployment Testing: Zero-downtime deployment validation

Acceptance Criteria:
├── Performance: All performance requirements met under load testing
├── Security: Security audit passed with no critical vulnerabilities
├── Integration: All integration points tested and validated
├── Monitoring: Complete observability stack operational
├── Documentation: Technical documentation complete and validated
```

**Requirements Traceability:**
```
Technical Requirements Mapping:
├── Business Requirement → Technical Requirement → Design Decision
├── Performance Goal → Load Test Scenario → Validation Criteria
├── Security Policy → Implementation Control → Testing Procedure
├── Integration Need → Technical Specification → Acceptance Test

Quality Assurance:
├── Code Review: Technical requirements compliance verification
├── Architecture Review: Design alignment with requirements
├── Performance Review: Benchmark achievement validation
├── Security Review: Compliance and vulnerability assessment
├── Documentation Review: Technical specification completeness
```

Evidence: Comprehensive technical analysis, quantified performance requirements, security framework, integration specifications, validation methodology
</example>
**Excellence Points**: +2400 (technical depth, quantified requirements, comprehensive security, validation framework)

## Key Patterns for Requirements Excellence

### Requirements Discovery Framework:
1. **Stakeholder Analysis**: Comprehensive identification and engagement of all affected parties
2. **Customer Research**: Direct customer input through interviews, surveys, and observation
3. **Current State Analysis**: Quantified assessment of existing systems and processes
4. **Future State Vision**: Clear definition of desired outcomes and success criteria
5. **Gap Analysis**: Systematic identification of requirements to bridge current and future states

### Requirements Quality Standards:
1. **Measurable Criteria**: Quantified acceptance criteria with objective validation
2. **Traceability**: Clear links between business needs, requirements, and implementation
3. **Completeness**: Comprehensive coverage of functional, non-functional, and constraint requirements
4. **Consistency**: Aligned requirements across all system components and interfaces
5. **Feasibility**: Validated technical and business feasibility for all requirements

### Validation and Verification:
1. **Stakeholder Review**: Systematic validation with all requirement stakeholders
2. **Prototype Validation**: Early validation through working prototypes and mockups
3. **Technical Feasibility**: Engineering validation of implementation approach
4. **Business Value**: Product management validation of business impact and priority
5. **Customer Acceptance**: Direct customer validation of requirements understanding

### Requirements Management:
1. **Living Documentation**: Continuously updated requirements with change management
2. **Version Control**: Systematic tracking of requirement changes and evolution
3. **Impact Analysis**: Assessment of change implications across all system components
4. **Communication**: Clear requirements communication to all development stakeholders
5. **Acceptance Tracking**: Systematic validation of requirement implementation

### Memory Integration Pattern:
Requirements excellence builds on understanding stakeholder needs, systematic discovery methods, and validation patterns that have proven effective across similar projects and domains.