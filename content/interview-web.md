---
title: Web & Frameworks Interview Questions
nav: Interview - Web
description: 25 web-layer interview questions - servlets, JSP, sessions, filters, Spring IoC/MVC/Boot, Hibernate, Struts, EJB, REST design.
section: Interview & Certification
order: 80
---

## Web & Frameworks - topic bank

Topic bank #7 of the [Interview Prep hub](interview.html). Tutorials: [Servlets & JSP](servlets-jsp.html) · [JSP tutorial](servlets-jsp.html) · [Spring](spring.html) · [Hibernate/JPA](hibernate-jpa.html) · [Struts](struts.html) · [EJB](ejb.html).

<details class="iq"><summary>1. Servlet lifecycle - who calls what and when?</summary>
<p>Container creates one instance per servlet (unless SingleThreadModel - avoid), calls <code>init(ServletConfig)</code> once, then <code>service()</code> per request (dispatching to doGet/doPost), then <code>destroy()</code> at shutdown. Consequences: servlet fields are shared across requests - never store per-request state in fields (the #1 servlet bug). <code>HttpServlet</code> is not thread-safe by design; your code must be.</p>
</details>

<details class="iq"><summary>2. GET vs POST semantics?</summary>
<p>GET: safe + idempotent, parameters in the query string (length limits, logged, cacheable) - for reads. POST: body params, not idempotent - for mutations. PUT/DELETE in REST: idempotent writes. Interview twist: java2s-era servlets put everything in doGet - explain why that breaks caches and bookmarks.</p>
</details>

<details class="iq"><summary>3. Forward vs redirect vs include?</summary>
<p>Forward (<code>RequestDispatcher.forward</code>): server-side, same request/response, URL unchanged - MVC pattern. Redirect (<code>sendRedirect</code>): 302/303, client makes a new request, URL changes, request attributes lost - use after POST (PRG pattern) to prevent resubmission. Include: merges another resource's output (headers: it's rendered inside).</p>
</details>

<details class="iq"><summary>4. Session management mechanics?</summary>
<p>Server creates an HttpSession, sets <code>JSESSIONID</code> cookie; subsequent requests carry it (URL rewriting fallback <code>;jsessionid=</code>). Sessions live in server memory by default - break in clusters unless sticky sessions or a shared store (Redis/DB). Timeout via web.xml/session config; invalidation for logout. Objects stored in a session must be Serializable for replication.</p>
</details>

<details class="iq"><summary>5. Cookies vs sessions - and security flags?</summary>
<p>Cookies are client-side key/values (size ~4KB, visible to user unless encrypted); sessions are server-side state keyed by cookie. Security flags: <code>HttpOnly</code> (no JS access), <code>Secure</code> (HTTPS only), <code>SameSite=Lax/Strict</code> (CSRF mitigation). Never store sensitive data (roles/price) in cookies without signing/encryption.</p>
</details>

<details class="iq"><summary>6. Filters vs listeners?</summary>
<p>Filters (Servlet spec) wrap requests/responses: auth, logging, encoding, CORS, compression - chained via FilterChain, can abort or modify. Listeners observe lifecycle: context/session/request events (SessionListener for online-user counts, ContextListener for startup init). Interceptors/Spring AOP are the framework-layer equivalents.</p>
</details>

<details class="iq"><summary>7. What does Spring's IoC container actually do?</summary>
<p>Reads configuration (annotations/Java config/XML), instantiates beans, wires dependencies (constructor/setter/field injection), applies post-processors (AOP proxies, @Autowired resolution, @Value), manages scopes (singleton default, prototype, request, session) and lifecycle callbacks. You get testability (inject mocks), decoupling, and one place to change wiring - the two core ideas are Dependency Injection and the container owning creation.</p>
</details>

<details class="iq"><summary>8. Constructor vs field injection?</summary>
<p>Constructor: dependencies explicit, final fields, fails fast, circular dependencies surface at startup, easy plain-Java tests (no container) - recommended default. Field/setter: convenient, but hidden dependencies, harder immutability and testing. Interviewers use this to check whether you've worked on real Spring codebases.</p>
</details>

<details class="iq"><summary>9. What is Spring AOP - how is it implemented?</summary>
<p>Cross-cutting concerns (transactions, security, logging, metrics) as aspects around join points. Implementation: runtime JDK dynamic proxies (interface-based) or CGLIB subclass proxies (class-based, default in Boot 2+). Consequences: self-invocation bypasses the proxy (calling <code>this.method()</code> skips @Transactional!), private/final methods can't be advised, and bean types may surprise casts.</p>
</details>

<details class="iq"><summary>10. @Transactional semantics you must know?</summary>
<p>Proxy-intercepted: propagation (REQUIRED default joins outer; REQUIRES_NEW suspends; NESTED uses savepoints), isolation, rollback rules (rolls back on RuntimeException, NOT on checked by default - set rollbackFor), readOnly hint, timeout. Pitfalls: self-invocation, exceptions swallowed, long transactions holding connections/locks, and mixing with async threads (transaction context is thread-bound).</p>
</details>

<details class="iq"><summary>11. Spring MVC request flow?</summary>
<p>DispatcherServlet → HandlerMapping finds the controller → HandlerAdapter invokes it (arguments resolved: @RequestParam/@PathVariable/@RequestBody via HttpMessageConverters) → return value handled (@ResponseBody → Jackson JSON, view name → ViewResolver) → exception resolvers (@ControllerAdvice) on error. One front controller, pluggable everything - that's the pattern.</p>
</details>

<details class="iq"><summary>12. Spring Boot auto-configuration and starters?</summary>
<p>@SpringBootApplication = @Configuration + @EnableAutoConfiguration + @ComponentScan. Auto-config classes are discovered from <code>META-INF/spring/...AutoConfiguration.imports</code> (Boot 3) and gated by @ConditionalOnClass/OnMissingBean etc. Starters bundle dependencies (spring-boot-starter-web = MVC + Jackson + Tomcat). Debug with <code>--debug</code> to see the condition-evaluation report - the interview gold answer.</p>
</details>

<details class="iq"><summary>13. How does Hibernate/JPA actually load and persist entities?</summary>
<p>Entities have states: transient → managed (persistence context) → detached → removed. The persistence context (first-level cache) guarantees identity within a transaction (same row = same object), dirty checking auto-flushes UPDATEs on commit, and flush modes control when SQL goes out. Lazy vs eager determines when associations load; LazyInitializationException = accessing a lazy proxy after the session closed (detached).</p>
</details>

<details class="iq"><summary>14. Why does Hibernate generate so many queries - the N+1 story?</summary>
<p>Load 100 orders, access order.customer each → 1 + 100 SELECTs. Fixes: join fetch in JPQL, EntityGraph, @BatchSize/</code>hibernate.default_batch_fetch_size</code> (IN-clause batching), or DTO projections. Detect by counting queries (<code>hibernate.generate_statistics</code>, datasource-proxy, p6spy). Also explain second-level cache (shared, opt-in) vs first-level (per session).</p>
</details>

<details class="iq"><summary>15. JPA merge vs persist vs save vs saveOrUpdate?</summary>
<p><code>persist</code>: INSERT, entity must be new (no id); <code>merge</code>: copies state onto a managed instance (SELECT + UPDATE for detached), returns the managed instance; <code>update</code> (Hibernate): reattach detached, throws if it exists? no - it forces update; <code>find/get</code>: by primary key. Spring Data <code>save()</code>: persist if new (isNew heuristic: null id) else merge. Know which SQL each produces - that's the answer they want.</p>
</details>

<details class="iq"><summary>16. Optimistic vs pessimistic locking in frameworks?</summary>
<p>Optimistic: @Version column, UPDATE ... WHERE version = n, throws OptimisticLockException on conflict - default for web apps (no locks held during user think time). Pessimistic: SELECT FOR UPDATE / LockModeType.PESSIMISTIC_WRITE - short critical sections only. Retry semantics differ: optimistic needs a user-visible retry path.</p>
</details>

<details class="iq"><summary>17. REST design rules - the ones interviewers score?</summary>
<p>Nouns not verbs (/orders/42 not /getOrder), correct verbs/status codes (201+Location on create, 404, 409 conflict, 422 validation, 204 delete), idempotency (PUT/DELETE repeatable), pagination (page/size or cursor), versioning strategy, HATEOAS optional, statelessness (no server sessions - tokens), and consistent error payloads (RFC 7807 problem+json).</p>
</details>

<details class="iq"><summary>18. Authentication for APIs - sessions vs JWT vs OAuth2?</summary>
<p>Sessions: server state, easy revocation, needs sticky/shared store. JWT: stateless, signed claims, revocation is the pain (short expiry + refresh tokens), never store secrets in payload (readable). OAuth2/OIDC: delegated auth for third parties; the modern flow is authorization code + PKCE. OWASP basics: hash passwords (bcrypt/argon2), HTTPS everywhere, rate limiting, generic login errors.</p>
</details>

<details class="iq"><summary>19. Struts action flow - legacy knowledge still asked?</summary>
<p>Request → ActionServlet (front controller) → ActionMapping (struts-config.xml) → ActionForm populated from params (validation) → Action.execute (business via delegate) → returns ActionForward → JSP/Tiles render. Value: recognizing front-controller + form-bean patterns that Spring MVC later streamlined; when asked "why modernization", point at XML config, per-action classes, and the 2014 CVE-2014-0050-era upgrade pressure.</p>
</details>

<details class="iq"><summary>20. EJB - the three bean types (legacy but examinable)?</summary>
<p>Session beans: stateless (pooled, no client state), stateful (conversational state bound to client), singleton (one per app, startup init). Message-driven beans: JMS listeners with container-managed transactions - async backbone. Add container services (transactions, security, pooling, timers) as the historical value proposition; modern equivalents are Spring beans + @Transactional.</p>
</details>

<details class="iq"><summary>21. How do you debug a slow request in production?</summary>
<p>Break down timings: access logs + APM (trace spans), thread dumps during slowness (jstack, blocked on DB/lock), slow query log, pool metrics (connections waiting), GC logs for pauses, and N+1 detection. Rule out the layers in order (network → proxy → app threads → DB → external calls) using evidence, not guesses.</p>
</details>

<details class="iq"><summary>22. Caching layers for a web app?</summary>
<p>Client/browser (Cache-Control, ETag), CDN (static assets), app-level (Caffeine in-process, bounded with TTL), distributed (Redis/Memcached - serialization + invalidation strategy), DB query cache (often counterproductive), plus HTTP caching semantics for APIs. Name the invalidation strategy per layer (TTL vs explicit) and what happens on cold start/thundering herd (cache stampede → mutex/lock).</p>
</details>

<details class="iq"><summary>23. How do you handle file uploads/downloads safely?</summary>
<p>Upload: multipart handling (Servlet 3.0 Part API / MultipartFile), enforce size limits (container + app), validate content type AND sniff bytes, store outside webroot with generated names, never trust the client filename (path traversal!), scan for malware, and stream to disk/object storage. Download: set Content-Disposition, avoid user-controlled paths, serve via signed URLs.</p>
</details>

<details class="iq"><summary>24. What is the deployment story: WAR vs executable JAR vs containers?</summary>
<p>WAR: build once, deploy into Tomcat/JBoss; container provides libs/classloader isolation - classic. Executable Spring Boot JAR: embedded server, one artifact, environment config externalized - modern default. Containers/K8s: image + config maps + health probes; 12-factor config via env vars, graceful shutdown, readiness vs liveness probes. Explain trade-offs: ops simplicity vs fine-grained container control.</p>
</details>

<details class="iq"><summary>25. Whiteboard: design a URL shortener's Java backend in 10 minutes?</summary>
<p>API: POST /links {url} → {code}; GET /{code} → 301/302. Storage: table (code PK, url, created_by, expires) or KV store; code = base62 of sequence or random with collision check. Read path cached (Redis + local Caffeine). Analytics async (queue). Concerns to mention unprompted: validation (URL schemes, SSRF), rate limiting, abuse/blocklist, expiry/cleanup job, and 301 vs 302 semantics (permanent caching trade-off).</p>
</details>

---

Hub: [Interview Prep home](interview.html) · Next: [Coding & puzzles](interview-coding.html) · Practice: [Test 3](ocjp-practice-3.html)
