# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A `market-data-feed-handler` is a low-latency market data feed handler. It keeps WebSocket connections to several crypto venues
(Binance, OKX, Kraken, etc...), decodes their feeds into one normalized binary format, assembles and verifies L2 order
books, and fans the result out to local consumers over message queue.


## Technology stack:

- C++23
- Qt/QML
- Boost.Asio
- CMake
- Conan
- ZeroMQ


## Architecture

### Application Structure

TBD

### Design documentation

TBD

### Key Components

To be defined...

## Development Philosophy

- Simplicity and readability over cleverness — write minimal code
- Start minimal, verify, then add complexity
- Keep core logic clean, push implementation details to edges
- Less Code = Less Debt
- Do not reinvent the wheel. Use existing battle-tested solutions when possible.
- A code must be fast, effective with minimal latency

## True Objective

Deliver what the user would have requested if they had thought about the problem more comprehensively:

1. First, complete all explicitly stated requirements
2. Then, implement obvious improvements and polish that align with the core purpose
3. In case of any design oversights in the original requirements, highlight and fix them
4. Ensure the solution is complete, robust, and user-friendly

## Claude Memory

If the user corrects you with an exclamation mark, keep his note in the memory to avoid the same mistake again.

## Completion Criteria

Work is considered complete when ALL of the following are true:

1. The solution includes reasonable improvements that align with the core purpose
2. Code is thoroughly tested, well-documented, and passes standard linting
3. Code is not only functional but clean, idiomatic, concise, and maintainable
4. Project structure is logical, with clear entry points and documentation

## Coding Standards

- Write comments in English
- Public functions first in classes, documented extensively; internal functions — a sentence or two
- Small focused functions
- Early returns
- The Single Level of Abstraction (SLA) principle: all statements within a function or method should operate at the same conceptual level—ranging from high-level business logic to low-level technical details
- name dicts, hash tables and any other key-value container key-first, in the order a lookup reads: `CODE_TO_NAME`, `DIVISION_TO_CATEGORY` — never `NAME_BY_CODE`, `CATEGORY_BY_DIVISION`. Applies to private maps and local variables too, not just constants.
- mark issues in existing code with "TODO:" prefix
- don't repeat yourself
- only modify code related to the task at hand

## Testing strategy

... TBD

## Development Commands

...TBD

## Commit Message Convention

Format: `<type>(<component>)[!]: <description>` (max 100 chars)
Valid types: `feat`, `fix`, `chore`, `build`, `docs`, `test`, `perf`, `style`, `refactor`, `ci`, `revert`
Examples: `feat(UI): add search filters`, `fix: resolve login timeout`, `feat!: breaking API change`
Versioning: `feat` bumps MINOR, `fix`/`perf`/`revert` bumps PATCH, `!` bumps MAJOR.

## Task Completion

Conclude the task is completed when:
- All completion criteria have been satisfied
- The entire solution reviewed for quality and consistency
- No obvious improvements left to implement

Approach tasks methodically, making multiple passes to refine the solution.
