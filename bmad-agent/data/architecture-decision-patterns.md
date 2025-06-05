# Architecture Decision Patterns

## Purpose
Define common architectural decisions to detect during brownfield analysis. This guide helps LLMs identify significant technical choices and understand their implications.

## Architecture Decision Categories

### 1. System Architecture Patterns

#### Monolithic Architecture
**Detection Signals**:
- Single deployable unit
- Shared database across all features
- Single build artifact (JAR, Docker image)
- Unified codebase without service boundaries

**Common Rationale**:
- Simplicity for small teams
- Easier debugging and testing
- Lower operational overhead
- Faster initial development

**Trade-offs to Document**:
- (+) Simple deployment and debugging
- (+) No network latency between components
- (-) Scaling challenges
- (-) Technology lock-in

#### Microservices Architecture
**Detection Signals**:
- Multiple repositories or mono-repo with service directories
- Service-specific databases
- API gateway or service mesh
- Inter-service communication patterns

**Common Rationale**:
- Independent scaling needs
- Team autonomy requirements
- Technology diversity benefits
- Fault isolation importance

**Trade-offs to Document**:
- (+) Independent deployment and scaling
- (+) Technology flexibility per service
- (-) Operational complexity
- (-) Network latency and reliability concerns

#### Serverless Architecture
**Detection Signals**:
- Lambda/Cloud Functions usage
- Event-driven triggers
- Managed services integration
- Pay-per-use configurations

**Common Rationale**:
- Cost optimization for variable loads
- Minimal operational overhead
- Automatic scaling requirements
- Event-driven use cases

**Trade-offs to Document**:
- (+) No server management
- (+) Automatic scaling
- (-) Vendor lock-in
- (-) Cold start latency

### 2. Data Architecture Patterns

#### SQL vs NoSQL Decision
**SQL Detection**:
- Relational databases (PostgreSQL, MySQL, SQL Server)
- Schema migration files
- ORM usage (Sequelize, SQLAlchemy, Hibernate)
- ACID transaction requirements

**NoSQL Detection**:
- Document stores (MongoDB, CouchDB)
- Key-value stores (Redis, DynamoDB)
- Graph databases (Neo4j)
- Column stores (Cassandra)

**Decision Factors to Extract**:
- Data consistency requirements
- Query complexity needs
- Scaling patterns (vertical vs horizontal)
- Schema flexibility requirements

#### Event Sourcing
**Detection Signals**:
- Event store implementation
- Event types/classes
- Projection/read model generation
- Command/Event separation

**Common Rationale**:
- Complete audit trail requirements
- Time-travel debugging needs
- Complex business logic tracking
- Multi-service data synchronization

#### CQRS (Command Query Responsibility Segregation)
**Detection Signals**:
- Separate read/write models
- Command handlers and query handlers
- Eventual consistency patterns
- Materialized views

**Common Rationale**:
- Read/write workload differences
- Complex query requirements
- Performance optimization needs
- Scalability requirements

### 3. API Architecture Patterns

#### REST API
**Detection Signals**:
- Resource-based URLs
- HTTP verbs usage (GET, POST, PUT, DELETE)
- JSON/XML responses
- OpenAPI/Swagger documentation

**Common Rationale**:
- Standard HTTP semantics
- Wide client support
- Stateless design benefits
- Caching capabilities

#### GraphQL API
**Detection Signals**:
- Schema definition files (.graphql)
- Resolvers implementation
- Single endpoint pattern
- Query/Mutation/Subscription types

**Common Rationale**:
- Flexible data fetching
- Reduced over/under-fetching
- Strong typing benefits
- Mobile optimization needs

#### gRPC/Protocol Buffers
**Detection Signals**:
- .proto files
- Generated code from protobuf
- Binary protocol usage
- Service definitions

**Common Rationale**:
- High performance requirements
- Strong typing across services
- Bi-directional streaming needs
- Polyglot environment support

### 4. Frontend Architecture Patterns

#### Single Page Application (SPA)
**Detection Signals**:
- Client-side routing
- JavaScript framework (React, Vue, Angular)
- API-driven data fetching
- Build process for bundling

**Common Rationale**:
- Rich interactive experience
- Reduced server load
- Mobile-like experience
- Frontend/backend separation

#### Server-Side Rendering (SSR)
**Detection Signals**:
- Next.js, Nuxt.js, Angular Universal
- Server-side template engines
- Initial HTML with hydration
- SEO optimizations

**Common Rationale**:
- SEO requirements
- Initial load performance
- Progressive enhancement
- Social media sharing needs

#### Micro-Frontends
**Detection Signals**:
- Module federation
- Independent frontend deployments
- iframe or Web Components usage
- Separate build pipelines

**Common Rationale**:
- Team autonomy
- Independent deployment needs
- Technology diversity
- Large application management

### 5. Infrastructure Architecture Patterns

#### Container Orchestration
**Detection Signals**:
- Kubernetes manifests
- Docker Compose files
- Helm charts
- Service mesh configuration

**Common Rationale**:
- Container management at scale
- Self-healing requirements
- Rolling deployment needs
- Resource optimization

#### Infrastructure as Code
**Detection Signals**:
- Terraform files
- CloudFormation templates
- Ansible playbooks
- Pulumi code

**Common Rationale**:
- Reproducible environments
- Version control for infrastructure
- Disaster recovery capability
- Multi-environment management

## Decision Extraction Template

### Standard Architecture Decision Record
```json
{
  "type": "architecture_decision",
  "id": "adr-{number}",
  "title": "Choice of {Technology/Pattern}",
  "status": "accepted|deprecated|superseded",
  "context": {
    "problem_statement": "What problem needed solving",
    "constraints": ["constraint1", "constraint2"],
    "assumptions": ["assumption1", "assumption2"]
  },
  "decision": {
    "choice": "What was chosen",
    "rationale": "Why this choice was made",
    "alternatives_considered": [
      {
        "option": "Alternative 1",
        "pros": ["pro1", "pro2"],
        "cons": ["con1", "con2"],
        "rejection_reason": "Why not chosen"
      }
    ]
  },
  "consequences": {
    "positive": ["benefit1", "benefit2"],
    "negative": ["drawback1", "drawback2"],
    "neutral": ["trade-off1", "trade-off2"]
  },
  "implementation": {
    "migration_required": true,
    "effort_estimate": "high|medium|low",
    "risks": ["risk1", "risk2"]
  },
  "metadata": {
    "decided_date": "2023-06-15",
    "decision_makers": ["architect", "tech-lead"],
    "review_date": "2024-06-15",
    "related_decisions": ["adr-001", "adr-003"]
  }
}
```

## Detection Heuristics

### Configuration Files
Look for architecture indicators in:
- `package.json` - Framework and library choices
- `docker-compose.yml` - Service architecture
- `k8s/*.yaml` - Deployment architecture
- `.env.example` - External service dependencies
- `terraform/*.tf` - Infrastructure choices

### Code Structure
Analyze architecture from:
- Directory organization
- Service boundaries
- Shared libraries
- Communication patterns
- Data flow paths

### Documentation
Extract decisions from:
- README files
- Architecture diagrams
- ADR documents
- Wiki pages
- Code comments with "Decision:", "Chose:", "Rationale:"

## Common Decision Patterns

### Performance Optimization Decisions
```json
{
  "pattern": "Caching Strategy",
  "common_choices": {
    "Redis": "For distributed caching with TTL",
    "In-Memory": "For single-instance applications",
    "CDN": "For static asset caching",
    "Database": "For query result caching"
  },
  "detection": "Look for cache libraries, Redis connections, cache headers"
}
```

### Security Architecture Decisions
```json
{
  "pattern": "Authentication Strategy",
  "common_choices": {
    "JWT": "Stateless authentication for APIs",
    "OAuth2": "Third-party integration needs",
    "Session": "Traditional web applications",
    "API Key": "Service-to-service auth"
  },
  "detection": "Auth middleware, token handling, session stores"
}
```

### Scalability Decisions
```json
{
  "pattern": "Scaling Strategy",
  "common_choices": {
    "Horizontal": "Stateless services, load balancers",
    "Vertical": "Database scaling, resource increase",
    "Auto-scaling": "Cloud provider integration",
    "Manual": "Predictable load patterns"
  },
  "detection": "Load balancer configs, auto-scaling rules, clustering"
}
```

## Quality Indicators

### Well-Documented Decisions
- Clear problem statement
- Multiple alternatives considered
- Trade-offs explicitly stated
- Success metrics defined
- Review timeline established

### Poorly Documented Decisions
- No rationale provided
- Single option considered
- No trade-off analysis
- Missing context
- No review plan

## Evolution Patterns

### Migration Decisions
Detect ongoing migrations:
- Old and new patterns coexisting
- Migration scripts or tools
- Feature flags for gradual rollout
- Deprecation warnings
- Dual-write patterns

### Deprecated Patterns
Identify abandoned approaches:
- Code marked as deprecated
- Alternative implementations present
- Migration guides in documentation
- Reduced usage over time
- Technical debt comments