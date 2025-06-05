# Bootstrap Analysis Examples

## Purpose
This file provides concrete examples of brownfield codebase analysis patterns to guide LLMs in performing effective memory bootstrap operations.

## Example 1: E-Commerce Platform Bootstrap

### Project Discovery
```
Project: FastShop E-Commerce Platform
Type: Full-stack web application
Age: 2.5 years
Team Size: 8-10 developers (inferred from commit history)
Active: High commit frequency, daily deployments
```

### Architectural Decision Extraction
```json
{
  "type": "decision",
  "decision": "Microservices over Monolith",
  "rationale": "Found separate services for inventory, orders, payments, and users with individual package.json files and deployment configs",
  "alternatives_considered": ["Monolith", "Serverless"],
  "evidence": "Separate repositories, docker-compose.yml with 6 services, API gateway pattern",
  "confidence": 0.95,
  "impact": "high",
  "project": "fastshop"
}
```

### Pattern Recognition Example
```json
{
  "type": "pattern",
  "pattern_name": "Repository Pattern for Data Access",
  "description": "All database operations go through repository classes with interfaces",
  "usage_count": 23,
  "effectiveness": 0.9,
  "example": "class UserRepository implements IUserRepository { async findById(id: string): Promise<User> { ... } }",
  "locations": ["services/users/repositories/", "services/orders/repositories/"],
  "project": "fastshop"
}
```

### Coding Style Extraction
```json
{
  "type": "preference", 
  "preference": "TypeScript with strict mode",
  "evidence_count": 156,
  "consistency": 0.98,
  "details": {
    "naming": "camelCase for functions, PascalCase for classes/interfaces",
    "files": "kebab-case for files, index.ts for directory exports",
    "imports": "Grouped by external, internal, types, with blank lines",
    "async": "async/await preferred over promises, no callbacks"
  },
  "project": "fastshop"
}
```

### Issue Documentation
```json
{
  "type": "issue",
  "issue": "N+1 query problem in order history endpoint",
  "severity": "high",
  "current_solution": "Added dataloader pattern but not consistently",
  "evidence": "TODO comments in order.service.ts, performance monitoring shows slow queries",
  "recommendation": "Implement dataloader pattern consistently across all services",
  "project": "fastshop"
}
```

## Example 2: Data Analytics Platform Bootstrap

### Technology Stack Discovery
```
Primary Language: Python 3.9
Framework: FastAPI + Pandas + Apache Spark
Database: PostgreSQL (OLTP) + Redshift (OLAP)
Testing: pytest with 78% coverage
Infrastructure: AWS with Terraform
Orchestration: Airflow for ETL pipelines
```

### Architectural Pattern Analysis
```json
{
  "type": "decision",
  "decision": "Lambda Architecture for real-time and batch processing",
  "rationale": "Separate paths for streaming (Kinesis) and batch (S3->Spark) with serving layer",
  "evidence": "Directory structure: streaming/, batch/, serving/, plus Kinesis configs",
  "alternatives_considered": ["Kappa architecture", "Traditional ETL"],
  "confidence": 0.85,
  "project": "analytics-platform"
}
```

### Workflow Pattern Detection
```json
{
  "type": "pattern",
  "pattern_name": "DAG-based ETL with comprehensive testing",
  "description": "Each Airflow DAG has corresponding test file with fixture data",
  "effectiveness": 0.95,
  "usage_count": 34,
  "example": "dags/customer_360.py -> tests/dags/test_customer_360.py",
  "benefits": "High reliability, easy debugging, confident deployments",
  "project": "analytics-platform"
}
```

### Team Preference Capture
```json
{
  "type": "preference",
  "category": "documentation",
  "preference": "Docstrings for every public function with Examples section",
  "evidence_count": 89,
  "consistency": 0.92,
  "example": "\"\"\"Calculate customer lifetime value.\n\nArgs:\n    customer_id: Unique identifier\n    \nReturns:\n    float: CLV in USD\n    \nExample:\n    >>> calculate_clv('cust-123')\n    1523.45\n\"\"\"",
  "project": "analytics-platform"
}
```

## Example 3: Mobile App Backend Bootstrap

### Quick Pattern Recognition
```
Analyzing: SocialConnect Mobile Backend
Time: 15 minutes (quick mode)

Top Patterns Found:
1. JWT with refresh tokens (confidence: 95%)
2. GraphQL with DataLoader (confidence: 90%)
3. Three-layer architecture (confidence: 98%)
4. Feature flags via LaunchDarkly (confidence: 100%)
5. Comprehensive request logging (confidence: 95%)
```

### Decision History Reconstruction
```json
{
  "type": "decision",
  "decision": "GraphQL over REST for mobile API",
  "rationale": "Mobile clients need flexible data fetching to minimize requests",
  "evidence": "schema.graphql, resolvers/, no REST endpoints except auth",
  "impact": "Reduced mobile data usage by 60% (from comments)",
  "timeline": "Migrated from REST 1 year ago based on git history",
  "confidence": 0.9,
  "project": "socialconnect"
}
```

## Example 4: Bootstrap Validation Dialogue

### User Confirmation Example
```
Bootstrap: "I found evidence you're using Event Sourcing for the order system - 
all state changes go through events like OrderCreated, OrderShipped. Is this correct?"

User: "Yes, but we're actually moving away from it. Too complex for our needs."

Bootstrap Memory Update:
{
  "type": "decision",
  "decision": "Migrating away from Event Sourcing",
  "rationale": "Complexity outweighs benefits for current scale",
  "status": "in-progress",
  "lesson_learned": "Event Sourcing overhead not justified for simple CRUD operations",
  "confidence": 1.0
}
```

### Pattern Clarification Example
```
Bootstrap: "I see you're using a Builder pattern extensively for test data creation.
Example: UserBuilder.withEmail('test@example.com').withRole('admin').build()
Is this a pattern you want to maintain?"

User: "Absolutely, it makes our tests much more readable and maintainable."

Bootstrap Memory Update:
{
  "type": "pattern",
  "pattern_name": "Test Data Builders",
  "description": "Fluent builder pattern for test object creation",
  "effectiveness": 0.95,
  "team_satisfaction": "high",
  "maintain": true
}
```

## Example 5: Complex Codebase Bootstrap

### Large Monorepo Analysis
```
Project: EnterpriseHub
Structure: Monorepo with 15 packages
Analysis approach: Incremental with checkpoints

Phase 1: Core packages (30 min)
- packages/core
- packages/auth  
- packages/api
Checkpoint saved: .bmad/bootstrap/checkpoint-1.json

Phase 2: Feature packages (25 min)
- packages/billing
- packages/analytics
- packages/notifications
- packages/search
Checkpoint saved: .bmad/bootstrap/checkpoint-2.json

Phase 3: Support packages (20 min)
- packages/ui-components
- packages/utils
- packages/testing-utils
Final results: .bmad/bootstrap/final-results.json
```

### Memory Relationship Mapping
```json
{
  "memory_relationships": [
    {
      "memory_1": "decision-microservices",
      "memory_2": "pattern-api-gateway",
      "relationship": "enables",
      "strength": 0.9
    },
    {
      "memory_1": "issue-performance-bottleneck",
      "memory_2": "decision-caching-strategy",
      "relationship": "solved-by",
      "strength": 0.85
    },
    {
      "memory_1": "preference-typescript",
      "memory_2": "pattern-type-safe-apis",
      "relationship": "requires",
      "strength": 0.95
    }
  ]
}
```

## Bootstrap Quality Examples

### High-Quality Memory
```json
{
  "type": "decision",
  "decision": "PostgreSQL with JSONB for flexible schemas",
  "rationale": "Need flexibility for user-defined fields without schema migrations",
  "evidence": "20+ tables use JSONB columns, migrations show evolution",
  "alternatives_considered": ["MongoDB", "DynamoDB", "Traditional columns"],
  "trade_offs": "Slightly slower queries but much faster development",
  "success_metrics": "Zero schema migration downtime in 18 months",
  "confidence": 0.95,
  "project": "flexapp"
}
```

### Low-Quality Memory (What to Avoid)
```json
{
  "type": "decision",
  "decision": "Using React",
  "rationale": "Popular framework",
  "evidence": "package.json has react",
  "confidence": 0.5
}
```
**Issues**: Too vague, no real rationale, no context, low confidence

## Bootstrap Edge Cases

### Mixed Technology Detection
```
Found: Both Express.js and Fastify routes
Analysis: Migration in progress from Express to Fastify
Evidence: 
- Newer routes use Fastify patterns
- TODO comments mention "migrate to Fastify"
- Both frameworks in package.json

Memory Created:
{
  "type": "decision",
  "decision": "Migrating from Express to Fastify",
  "status": "in-progress",
  "progress": "approximately 60% based on route analysis",
  "rationale": "Performance improvements needed for scale",
  "confidence": 0.8
}
```

### Contradictory Patterns
```
Found: Multiple state management approaches
- Redux in older components
- Context API in newer components  
- Local state in some areas

Analysis: Evolutionary architecture without cleanup
Recommendation: Document intended approach and plan consolidation
```

## Success Metrics

### Effective Bootstrap Indicators
1. **Specific rationales** extracted for decisions
2. **Quantified pattern usage** (not just "found pattern")
3. **Clear evidence** for each finding
4. **Actionable insights** generated
5. **Realistic confidence scores** (not all 100%)

### Bootstrap Completeness Checklist
- [ ] Major architectural decisions captured (3-5 minimum)
- [ ] Coding patterns documented with examples (5-10)
- [ ] Team preferences extracted (3-5)
- [ ] Known issues mapped with context (if any)
- [ ] Technology choices understood with rationale
- [ ] Workflow patterns identified
- [ ] Memory relationships established
- [ ] Confidence scores assigned appropriately