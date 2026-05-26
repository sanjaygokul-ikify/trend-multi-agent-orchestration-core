## Contribution Guidelines
1. All PRs require architecture validation in docs/rfcs/
2. Implementations must pass chaos engineering tests (see .github/workflows/chaos.yml)
3. Performance characteristics must be documented

## Local Development
1. `make dev` starts test cluster
2. `make validate` runs static analysis
3. `make benchmark` runs microbenchmark suite