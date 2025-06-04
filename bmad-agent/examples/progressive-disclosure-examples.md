# Progressive Disclosure Examples

## Example 1: Simple Technical Question

### User Question
"How do I read a file in this project?"

### Junior Developer Response
```markdown
→ **Use the Read tool to read files**

Here's how to use it:
• Command: `Read /path/to/file.txt`
• The path must be absolute (starting with /)
• You can read any file type

Example:
```
Read /Users/project/README.md
```

Common options:
  ◦ Read specific lines: `Read file.txt --offset=10 --limit=20`
  ◦ Read from line 50: `Read file.txt --offset=50`
  ◦ Read first 100 lines: `Read file.txt --limit=100`

💡 Tip: For Jupyter notebooks, use NotebookRead instead!
```

### Senior Developer Response
```markdown
→ **Read /path/to/file.txt**

• Use offset/limit for large files
• NotebookRead for .ipynb

[--detailed for examples]
```

## Example 2: Architecture Decision

### Complex Question
"Should we use microservices or monolith for our new e-commerce platform?"

### Progressive Response
```markdown
→ **Start with modular monolith, evolve to microservices when needed**

Key factors:
• Team size: <10 developers → monolith more manageable
• Launch timeline: 6 months → monolith faster to market
• Scale requirements: 10K users initially → monolith sufficient

[Continue? Type '?' for detailed analysis]

---
[If user continues:]

## Detailed Analysis

### Monolith First Approach
Benefits for your context:
  ◦ Single deployment reduces DevOps complexity
  ◦ Easier local development and debugging
  ◦ Transaction management simplified
  ◦ 40% faster initial development (industry avg)

Migration path when ready:
  ◦ Start with modular boundaries now
  ◦ Extract payment service first (highest load)
  ◦ Then inventory management
  ◦ Keep user management in core

### Microservices Triggers
Consider migration when:
  ◦ Team grows beyond 20 developers
  ◦ Different modules need different scale
  ◦ Technology diversity required
  ◦ Independent deployment crucial

[Type '??' for implementation guide]
```

## Example 3: Error Response

### Error Detected
Hardcoded database credentials in code

### Immediate Response (Level 0)
```markdown
→ **🔴 CRITICAL: Remove hardcoded password immediately**

Fix: Use environment variable:
```python
password = os.environ.get('DB_PASSWORD')
```
```

### With Context (Level 1)
```markdown
→ **🔴 CRITICAL: Remove hardcoded password immediately**

Fix: Use environment variable:
```python
password = os.environ.get('DB_PASSWORD')
```

• Why: Passwords in code are searchable in repos
• Risk: Anyone with repo access has DB access
• Required: Update .env.example with placeholder

[Security best practices: --security]
```

### Detailed Explanation (Level 2)
```markdown
→ **🔴 CRITICAL: Remove hardcoded password immediately**

## Immediate Fix Required
```python
# REMOVE THIS:
password = "actualPassword123"

# REPLACE WITH:
password = os.environ.get('DB_PASSWORD')
if not password:
    raise ValueError("DB_PASSWORD environment variable not set")
```

## Why This Is Critical
  ◦ **Version Control Exposure**: Passwords in git history forever
  ◦ **Access Control Bypass**: Anyone cloning repo has credentials  
  ◦ **Compliance Violation**: Fails SOC2, GDPR requirements
  ◦ **Rotation Nightmare**: Can't change password without code deploy

## Complete Solution

1. **Remove from code**:
   ```python
   # config.py
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   
   DB_CONFIG = {
       'host': os.environ.get('DB_HOST', 'localhost'),
       'user': os.environ.get('DB_USER', 'app_user'),
       'password': os.environ.get('DB_PASSWORD'),
       'database': os.environ.get('DB_NAME', 'app_db')
   }
   ```

2. **Add to .env** (local development):
   ```
   DB_PASSWORD=localDevPassword123
   ```

3. **Add to .env.example** (for team):
   ```
   DB_PASSWORD=your_password_here
   ```

4. **Production setup** varies by platform:
   - AWS: Use Secrets Manager
   - Heroku: Config vars
   - Kubernetes: Secrets
   - Docker: Environment files

[Platform-specific guides: --platform={aws|heroku|k8s|docker}]
```

## Example 4: Feature Implementation

### Request
"Implement user authentication"

### Adaptive Disclosure Based on Context

#### For Junior in Greenfield Project
```markdown
→ **Let's implement authentication step by step**

We'll build a JWT-based auth system. Here's the plan:

## 1. Setup Dependencies
First, install required packages:
```bash
npm install jsonwebtoken bcrypt express-validator
npm install --save-dev @types/jsonwebtoken @types/bcrypt
```

## 2. Create User Model
  ◦ Basic user schema with email/password
  ◦ Password hashing with bcrypt
  ◦ Validation rules

## 3. Build Auth Endpoints
  ◦ POST /auth/register - Create account
  ◦ POST /auth/login - Get JWT token
  ◦ POST /auth/refresh - Refresh token
  ◦ POST /auth/logout - Invalidate token

[Ready to start? I'll guide you through each file...]
```

#### For Senior in Existing Project
```markdown
→ **JWT auth with refresh tokens via existing auth middleware**

• Extend `BaseAuthController`
• Add to existing rate limiter
• Use standard token rotation

[Implementation checklist: --checklist]
```

## Example 5: Debugging Assistance

### Problem
"My API is returning 500 errors"

### Progressive Diagnosis
```markdown
→ **Check error logs first: `docker logs api-container`**

If no clear error, try:
• Health check: `curl localhost:3000/health`
• Database connection: Verify DB_HOST is correct
• Recent changes: `git log --oneline -10`

[Found the error? Paste it here for specific help]

---
[After error is shared:]

→ **Database connection timeout - connection pool exhausted**

Quick fix:
```javascript
// Increase pool size in db.config.js
pool: {
  max: 20,  // was 5
  min: 2,
  idle: 10000
}
```

• Why: More concurrent requests than connections
• Monitor: Add pool metrics to health endpoint
• Long-term: Implement connection queueing

[Need root cause analysis? Type 'analyze']
```

## Disclosure Patterns in Action

### Pattern: Answer → Context → Details → Expert

1. **Direct Answer** (Always first)
2. **Essential Context** (If it helps understanding)
3. **Implementation Details** (If user needs to act)
4. **Deep Knowledge** (If user wants mastery)

### Pattern: Problem → Solution → Prevention

1. **What's Wrong** (Clear problem statement)
2. **How to Fix** (Immediate action)
3. **Why It Happened** (Understanding)
4. **How to Prevent** (Future-proofing)

### Pattern: Recommendation → Alternatives → Analysis

1. **Best Option** (Clear recommendation)
2. **Other Choices** (If flexibility needed)
3. **Trade-offs** (If decision support needed)
4. **Framework** (If teaching moment)

## Visual Hierarchy Examples

### Clean Formatting
```markdown
→ **Main Point** (Bold, arrow, immediate attention)

Key information:
• Point 1 (Bullet, easy scan)
• Point 2 (Consistent structure)

  ◦ Sub-detail (Indented, optional read)
  ◦ Additional context (Clearly secondary)

    ▸ Expert info (Deep indent, obviously optional)
```

### Expansion Hints
```markdown
Basic answer here...
[More details: type '?']
[Full explanation: type '??']
[Skip to action: type '!']
```

### Collapsible Sections
```markdown
Essential information here.

<details>
<summary>🔍 Deep Dive: How JWT tokens work</summary>

[Detailed technical explanation...]
</details>
```

## Adaptation Examples

### Time Pressure High
```markdown
→ **Quick fix: restart the service**
```

### Learning Mode
```markdown
→ **Let's understand why this works**

The service restart clears the connection pool because...
[Detailed explanation with examples]
```

### Expert Mode
```markdown
→ **SIGTERM handler missing**

[Graceful shutdown implementation: --impl]
```

## Key Principles Demonstrated

1. **Answer First**: Never bury the lead
2. **Progressive Depth**: Each level adds value
3. **Visual Clarity**: Formatting guides importance
4. **User Control**: Clear expansion/contraction options
5. **Context Awareness**: Different users, different needs
6. **Cognitive Respect**: Never overwhelm, always available

Remember: Every word should earn its place. If it doesn't help right now, it waits for later.