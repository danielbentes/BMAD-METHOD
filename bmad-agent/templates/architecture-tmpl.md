# {Project Name} Architecture Document

## Document Metadata & Evidence Trail

| Field | Value | Evidence |
|-------|-------|----------|
| Version | {1.0.0} | [ ] Version control tracked |
| Last Updated | {Date} | [ ] All sections current |
| UDTM Analysis | {Date} | [ ] 90+ minute analysis completed |
| Quality Gates | {Status} | [ ] All gates passed |
| Validation Status | {Status} | [ ] Peer review completed |

## Introduction / Preamble

{This document outlines the overall project architecture, including backend systems, shared services, and non-UI specific concerns. Its primary goal is to serve as the guiding architectural blueprint for AI-driven development, ensuring consistency and adherence to chosen patterns and technologies.

**Relationship to Frontend Architecture:**
If the project includes a significant user interface, a separate Frontend Architecture Document (typically named `front-end-architecture-tmpl.txt` or similar, and linked in the "Key Reference Documents" section) details the frontend-specific design and MUST be used in conjunction with this document. Core technology stack choices documented herein (see "Definitive Tech Stack Selections") are definitive for the entire project, including any frontend components.}

## Table of Contents

{ Update this if sections and subsections are added or removed }

## Technical Summary

{ Provide a brief paragraph overview of the system's architecture, key components, technology choices, and architectural patterns used. Reference the goals from the PRD. }

### Evidence Requirements
- [ ] PRD goals referenced and linked
- [ ] Key metrics defined
- [ ] Success criteria established

## High-Level Overview

{ Describe the main architectural style (e.g., Monolith, Microservices, Serverless, Event-Driven), reflecting the decision made in the PRD. Explain the repository structure (Monorepo/Polyrepo). Explain the primary user interaction or data flow at a conceptual level. }

{ Insert high-level mermaid system context or interaction diagram here - e.g., Mermaid Class C4 Models Layer 1 and 2 }

### Architecture Decision Records (ADRs)

#### ADR-001: Overall Architecture Style

| Decision | {Architecture Style} |
|----------|---------------------|
| Status | {Proposed/Accepted/Deprecated} |
| Date | {Date} |
| Context | {Why this decision was needed} |
| Decision | {What was decided} |
| Consequences | {Positive and negative impacts} |
| Alternatives Considered | {Other options evaluated} |

**Evidence Package:**
- [ ] Performance benchmarks comparing alternatives
- [ ] Scalability analysis documentation
- [ ] Cost comparison spreadsheet
- [ ] Team capability assessment
- [ ] Risk analysis matrix

## Architectural / Design Patterns Adopted

{ List the key high-level patterns chosen for the architecture. These foundational patterns should be established early as they guide component design, interactions, and technology choices. }

### Pattern Evaluation Matrix

| Pattern | Pros | Cons | Evidence | Risk Score |
|---------|------|------|----------|------------|
| **Pattern 1:** {e.g., Microservices} | {List pros} | {List cons} | {Research/benchmarks} | {1-10} |
| **Pattern 2:** {e.g., Event-Driven} | {List pros} | {List cons} | {Research/benchmarks} | {1-10} |
| **Pattern N:** {...} | {...} | {...} | {...} | {...} |

### Pattern Validation Checklist
- [ ] Industry best practices reviewed
- [ ] Similar successful implementations studied
- [ ] Anti-pattern analysis completed
- [ ] Team expertise assessed
- [ ] Migration path defined

## Component View

{ Describe the major logical components or services of the system and their responsibilities, reflecting the decided overall architecture (e.g., distinct microservices, modules within a monolith, packages within a monorepo) and the architectural patterns adopted. Explain how they collaborate. }

### Component Evidence Requirements

For each component:
- [ ] Responsibility clearly defined
- [ ] Interfaces documented
- [ ] Dependencies mapped
- [ ] Performance requirements specified
- [ ] Scalability approach validated

- Component A: {Description of responsibility}

{Insert component diagram here if it helps - e.g., using Mermaid graph TD or C4 Model Container/Component Diagram}

### Component Performance Benchmarks

| Component | Latency Target | Throughput Target | Evidence | Validation Method |
|-----------|----------------|-------------------|----------|-------------------|
| Component A | <100ms | 1000 req/s | {Load test results} | {Tool used} |
| Component B | <200ms | 500 req/s | {Benchmark data} | {Tool used} |

## Project Structure

{Provide an ASCII or Mermaid diagram representing the project's folder structure.}

```plaintext
{project-root}/
├── .github/                    # CI/CD workflows (e.g., GitHub Actions)
│   └── workflows/
│       └── main.yml
├── .vscode/                    # VSCode settings (optional)
│   └── settings.json
├── build/                      # Compiled output (if applicable, often git-ignored)
├── config/                     # Static configuration files (if any)
├── docs/                       # Project documentation (PRD, Arch, etc.)
│   ├── index.md
│   └── ... (other .md files)
├── infra/                      # Infrastructure as Code (e.g., CDK, Terraform)
│   └── lib/
│   └── bin/
├── node_modules/ / venv / target/ # Project dependencies (git-ignored)
├── scripts/                    # Utility scripts (build, deploy helpers, etc.)
├── src/                        # Application source code
│   ├── backend/                # Backend-specific application code (if distinct frontend exists)
│   │   ├── core/               # Core business logic, domain models
│   │   ├── services/           # Business services, orchestrators
│   │   ├── adapters/           # Adapters to external systems (DB, APIs)
│   │   ├── controllers/ / routes/ # API endpoint handlers
│   │   └── main.ts / app.py    # Backend application entry point
│   ├── frontend/               # Placeholder: See Frontend Architecture Doc for details if used
│   ├── shared/ / common/       # Code shared (e.g., types, utils, domain models if applicable)
│   │   └── types/
│   └── main.ts / index.ts / app.ts # Main application entry point (if not using backend/frontend split above)
├── stories/                    # Generated story files for development (optional)
│   └── epic1/
├── test/                       # Automated tests
│   ├── unit/                   # Unit tests (mirroring src structure)
│   ├── integration/            # Integration tests
│   └── e2e/                    # End-to-end tests
├── .env.example                # Example environment variables
├── .gitignore                  # Git ignore rules
├── package.json / requirements.txt / pom.xml # Project manifest and dependencies
├── tsconfig.json / pyproject.toml # Language-specific configuration (if applicable)
├── Dockerfile                  # Docker build instructions (if applicable)
└── README.md                   # Project overview and setup instructions
```

### Structure Validation
- [ ] Follows industry standards for chosen stack
- [ ] Supports scalability requirements
- [ ] Enables proper separation of concerns
- [ ] Facilitates testing approach
- [ ] Aligns with CI/CD strategy

## API Reference

### External APIs Consumed

{Repeat this section for each external API the system interacts with.}

#### {External Service Name} API

- **Purpose:** {Why does the system use this API?}
- **Base URL(s):**
  - Production: `{URL}`
  - Staging/Dev: `{URL}`
- **Authentication:** {Describe method}
- **Key Endpoints Used:**
  - **`{HTTP Method} {/path/to/endpoint}`:**
    - Description: {What does this endpoint do?}
    - Request Parameters: {Query params, path params}
    - Request Body Schema: {Provide JSON schema inline}
    - Example Request: `{Code block}`
    - Success Response Schema (Code: `200 OK`): {Provide JSON schema inline}
    - Error Response Schema(s) (Codes: `4xx`, `5xx`): {Provide JSON schema inline}
    - Example Response: `{Code block}`
- **Rate Limits:** {If known}
- **SLA:** {If available}
- **Link to Official Docs:** {URL}

#### API Integration Evidence
- [ ] API documentation reviewed
- [ ] Rate limits tested
- [ ] Error scenarios handled
- [ ] Retry logic implemented
- [ ] Circuit breaker configured
- [ ] Monitoring established

### Internal APIs Provided (If Applicable)

{If the system exposes its own APIs.}

#### {Internal API / Service Name} API

- **Purpose:** {What service does this API provide?}
- **Base URL(s):** {e.g., `/api/v1/...`}
- **Authentication/Authorization:** {Describe how access is controlled}
- **Endpoints:**
  - **`{HTTP Method} {/path/to/endpoint}`:**
    - Description: {What does this endpoint do?}
    - Request Parameters: {...}
    - Request Body Schema: {Provide JSON schema inline}
    - Success Response Schema (Code: `200 OK`): {Provide JSON schema inline}
    - Error Response Schema(s) (Codes: `4xx`, `5xx`): {Provide JSON schema inline}

#### API Performance Requirements
| Endpoint | Latency (p95) | Throughput | Evidence |
|----------|---------------|------------|----------|
| POST /api/v1/users | <200ms | 100 req/s | {Load test link} |
| GET /api/v1/products | <100ms | 1000 req/s | {Benchmark data} |

## Data Models

### Core Application Entities / Domain Objects

{Define the main objects/concepts the application works with.}

#### {Entity Name, e.g., User, Order, Product}

- **Description:** {What does this entity represent?}
- **Schema / Interface Definition:**
  ```typescript
  // Example using TypeScript Interface
  export interface {EntityName} {
    id: string; // {Description, e.g., Unique identifier}
    propertyName: string; // {Description}
    optionalProperty?: number; // {Description}
    // ... other properties
  }
  ```
- **Validation Rules:** {List any specific validation rules}
- **Performance Considerations:** {Index requirements, query patterns}

### Data Model Evidence
- [ ] Domain model reviewed by domain experts
- [ ] Scalability analysis completed
- [ ] Query patterns analyzed
- [ ] Index strategy defined
- [ ] Data growth projections calculated

### Database Schemas (If applicable)

{If using a database, define table structures or document database schemas.}

#### {Table / Collection Name}

- **Purpose:** {What data does this table store?}
- **Schema Definition:**
  ```sql
  -- Example SQL
  CREATE TABLE {TableName} (
    id VARCHAR(36) PRIMARY KEY,
    column_name VARCHAR(255) NOT NULL,
    numeric_column DECIMAL(10, 2),
    -- ... other columns, indexes, constraints
  );
  ```
- **Index Strategy:** {Define indexes and rationale}
- **Partitioning Strategy:** {If applicable}
- **Backup Strategy:** {RPO/RTO requirements}

### Database Performance Validation
- [ ] Query execution plans analyzed
- [ ] Load testing completed
- [ ] Index effectiveness validated
- [ ] Backup/restore tested
- [ ] Failover procedures verified

## Core Workflow / Sequence Diagrams

{ Illustrate key or complex workflows using mermaid sequence diagrams. }

### Workflow Performance Requirements

| Workflow | End-to-End Latency | Success Rate | Evidence |
|----------|-------------------|--------------|----------|
| User Registration | <3s | >99.9% | {Test results} |
| Order Processing | <5s | >99.5% | {Monitoring data} |

## Definitive Tech Stack Selections

{ This section outlines the definitive technology choices for the project. }

### Technology Evaluation Framework

For each technology choice, provide:
1. **Requirements Analysis** - What specific needs does this address?
2. **Options Evaluated** - What alternatives were considered?
3. **Evaluation Criteria** - How were options assessed?
4. **Evidence** - Benchmarks, POCs, research
5. **Decision Rationale** - Why this choice?
6. **Risk Assessment** - What could go wrong?

### Technology Decision Matrix

| Category | Technology | Version | Evidence | Risk Mitigation |
|----------|------------|---------|----------|-----------------|
| **Languages** | {e.g., TypeScript} | {e.g., 5.x} | {Benchmark results} | {Training plan} |
| **Runtime** | {e.g., Node.js} | {e.g., 22.x} | {Performance tests} | {Version strategy} |
| **Frameworks** | {e.g., NestJS} | {e.g., 10.x} | {POC results} | {Migration plan} |
| **Databases** | {e.g., PostgreSQL} | {e.g., 15} | {Load test data} | {HA strategy} |
| **Cloud Platform** | {e.g., AWS} | {N/A} | {Cost analysis} | {Multi-cloud plan} |

### Technology Validation Checklist
- [ ] All choices have documented evidence
- [ ] Performance requirements validated
- [ ] Team skills assessment completed
- [ ] Migration strategies defined
- [ ] Vendor lock-in risks assessed
- [ ] Total cost of ownership calculated

## Infrastructure and Deployment Overview

### Infrastructure Requirements Evidence

| Requirement | Target | Evidence | Validation Method |
|-------------|--------|----------|-------------------|
| Availability | 99.9% | {HA design docs} | {Chaos testing} |
| Scalability | 10x growth | {Load test results} | {Auto-scaling tests} |
| Security | SOC2 compliant | {Audit report} | {Pen testing} |
| Performance | <200ms p95 | {Benchmarks} | {Monitoring} |

- Cloud Provider(s): {e.g., AWS, Azure, GCP}
- Core Services Used: {List key managed services}
- Infrastructure as Code (IaC): {Tool used}
- Deployment Strategy: {e.g., Blue/Green}
- Environments: {List environments}
- Environment Promotion: {Describe steps}
- Rollback Strategy: {e.g., Automated rollback}

### Deployment Evidence
- [ ] IaC templates tested
- [ ] Deployment automation verified
- [ ] Rollback procedures tested
- [ ] Monitoring configured
- [ ] Alerts defined
- [ ] Runbooks created

## Error Handling Strategy

### Error Handling Evidence Requirements

- [ ] Error taxonomy defined
- [ ] Logging standards documented
- [ ] Retry policies tested
- [ ] Circuit breakers configured
- [ ] Error recovery procedures validated
- [ ] User communication templates created

- **General Approach:** {e.g., Use exceptions as primary mechanism}
- **Logging:**
  - Library/Method: {e.g., Structured logging with JSON}
  - Format: {e.g., JSON with correlation ID}
  - Levels: {e.g., DEBUG, INFO, WARN, ERROR, CRITICAL}
  - Context: {What contextual information must be included?}
- **Specific Handling Patterns:**
  - External API Calls: {Define retry mechanisms}
  - Internal Errors: {How to handle business logic exceptions}
  - Transaction Management: {Approach to ensure data consistency}

## Coding Standards

{These standards are mandatory for all code generation.}

### Standards Validation
- [ ] Linter configurations defined
- [ ] Code review checklist created
- [ ] Style guide documented
- [ ] Examples provided
- [ ] Automation configured
- [ ] Training materials prepared

[Previous coding standards content remains but with validation checkboxes added for each major section]

## Overall Testing Strategy

### Testing Requirements Evidence

| Test Type | Coverage Target | Current | Evidence | Gap Analysis |
|-----------|----------------|---------|----------|--------------|
| Unit | 80% | {X%} | {Report link} | {Actions} |
| Integration | 70% | {X%} | {Report link} | {Actions} |
| E2E | Critical paths | {X%} | {Test list} | {Actions} |
| Performance | All endpoints | {X%} | {Results} | {Actions} |
| Security | OWASP Top 10 | {X%} | {Scan report} | {Actions} |

### Testing Evidence Checklist
- [ ] Test strategy reviewed and approved
- [ ] Test environments provisioned
- [ ] Test data strategy defined
- [ ] Continuous testing implemented
- [ ] Test results tracking established
- [ ] Quality gates configured

## Security Best Practices

### Security Assessment Evidence

| Security Control | Implementation | Evidence | Validation |
|-----------------|----------------|----------|------------|
| Input Validation | {Library/method} | {Code review} | {Pen test} |
| Authentication | {Method} | {Audit trail} | {Security review} |
| Authorization | {RBAC/ABAC} | {Matrix document} | {Access review} |
| Encryption | {At rest/transit} | {Cert details} | {Scan results} |
| Secrets Management | {Tool} | {Rotation logs} | {Audit report} |

### Security Validation Checklist
- [ ] Threat model created and reviewed
- [ ] Security requirements traced to implementation
- [ ] Penetration testing scheduled
- [ ] Security monitoring configured
- [ ] Incident response plan created
- [ ] Compliance requirements mapped

## Performance Requirements & Validation

### Performance Benchmarks

| Metric | Requirement | Measured | Evidence | Status |
|--------|-------------|----------|----------|--------|
| Response Time (p95) | <200ms | {Xms} | {Test link} | {Pass/Fail} |
| Throughput | 1000 req/s | {X req/s} | {Load test} | {Pass/Fail} |
| Error Rate | <0.1% | {X%} | {Monitoring} | {Pass/Fail} |
| Resource Usage | <80% CPU | {X%} | {Metrics} | {Pass/Fail} |

### Scalability Validation

| Scenario | Target | Result | Evidence | Notes |
|----------|--------|--------|----------|-------|
| Normal Load | 100 users | {Result} | {Test data} | {Notes} |
| Peak Load | 1000 users | {Result} | {Test data} | {Notes} |
| Spike Test | 10x spike | {Result} | {Test data} | {Notes} |
| Endurance | 24 hours | {Result} | {Test data} | {Notes} |

## Cost Analysis & Optimization

### Total Cost of Ownership (TCO)

| Component | Monthly Cost | Annual Cost | Evidence | Optimization |
|-----------|--------------|-------------|----------|--------------|
| Infrastructure | ${X} | ${Y} | {Invoice} | {Options} |
| Licensing | ${X} | ${Y} | {Contracts} | {Options} |
| Operations | ${X} | ${Y} | {Estimates} | {Options} |
| **Total** | **${X}** | **${Y}** | - | - |

### Cost Optimization Evidence
- [ ] Right-sizing analysis completed
- [ ] Reserved instance strategy defined
- [ ] Auto-scaling policies optimized
- [ ] Unused resources identified
- [ ] Cost allocation tags implemented
- [ ] Budget alerts configured

## Compliance & Audit Requirements

### Compliance Matrix

| Requirement | Standard | Implementation | Evidence | Status |
|-------------|----------|----------------|----------|--------|
| Data Privacy | GDPR | {Approach} | {Audit doc} | {Compliant} |
| Security | SOC2 | {Controls} | {Report} | {In Progress} |
| Accessibility | WCAG 2.1 AA | {Testing} | {Report} | {Compliant} |
| Industry | {Standard} | {Approach} | {Evidence} | {Status} |

### Audit Trail Requirements
- [ ] All architectural decisions documented
- [ ] Change control process implemented
- [ ] Access logs retained per policy
- [ ] Regular compliance reviews scheduled
- [ ] Evidence repository maintained
- [ ] Audit findings tracking system

## Risk Register

### Technical Risks

| Risk | Probability | Impact | Mitigation | Evidence | Owner |
|------|-------------|--------|------------|----------|-------|
| {Risk 1} | {H/M/L} | {H/M/L} | {Strategy} | {Validation} | {Name} |
| {Risk 2} | {H/M/L} | {H/M/L} | {Strategy} | {Validation} | {Name} |

### Risk Validation
- [ ] All risks have mitigation strategies
- [ ] Risk owners assigned and acknowledged
- [ ] Mitigation effectiveness tested
- [ ] Residual risk accepted by stakeholders
- [ ] Risk review schedule established

## Quality Gates

### Architecture Quality Gates

| Gate | Criteria | Evidence Required | Status |
|------|----------|------------------|--------|
| Design Review | Pattern compliance | Review notes | {Pass/Fail} |
| Performance | Meets all targets | Test results | {Pass/Fail} |
| Security | No critical issues | Scan report | {Pass/Fail} |
| Scalability | 10x headroom | Load tests | {Pass/Fail} |
| Cost | Within budget | TCO analysis | {Pass/Fail} |

## Key Reference Documents

| Document | Purpose | Location | Status |
|----------|---------|----------|--------|
| PRD | Requirements | {Link} | {Current} |
| Frontend Architecture | UI Design | {Link} | {Current} |
| Security Assessment | Threat Model | {Link} | {Current} |
| Performance Test Results | Benchmarks | {Link} | {Current} |

## UDTM Analysis Record

### Critical Architecture Decisions

| Decision | Analysis Date | Participants | Confidence | Evidence Package |
|----------|--------------|--------------|------------|------------------|
| {Decision 1} | {Date} | {Names} | {95%+} | {Link to analysis} |
| {Decision 2} | {Date} | {Names} | {95%+} | {Link to analysis} |

## Change Log

| Change | Date | Version | Description | Author | Evidence | Review |
|--------|------|---------|-------------|--------|----------|---------|
| Initial | {Date} | 1.0.0 | Initial architecture | {Name} | {Links} | {Reviewers} |

## Document Validation Checklist

### Completeness Check
- [ ] All sections populated with evidence
- [ ] All decisions backed by data
- [ ] All risks identified and mitigated
- [ ] All requirements traced to implementation
- [ ] All validations completed

### Quality Score
- Evidence completeness: ___/100
- Validation coverage: ___/100
- Risk mitigation: ___/100
- Compliance readiness: ___/100
- **Overall Score**: ___/100

### Sign-offs
- [ ] Technical Lead: _________________ Date: _______
- [ ] Security Lead: _________________ Date: _______
- [ ] Operations Lead: ________________ Date: _______
- [ ] Product Owner: _________________ Date: _______

--- Below, Prompt for Design Architect (If Project has UI) To Produce Front End Architecture ----