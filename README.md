# Advanced Database Manipulation with Python using DuckDB

**Yang Wang**  
**ATUA – 2026**

[Slides is here](https://github.com/YangWang-Glasgow/DuckDB-and-Spatial-Functions/blob/a754925bded771f724b0e34ba36bbabb0524964d/Advanced%20Database%20Manipulation%20with%20Python%20using%20DuckDB.pptx)  

---

## 1. Database and Spatial Databases

### General Databases
- Collecting, storing, and using data securely and efficiently  
- Support informed decision-making  

**Examples**
- ArcGIS → File Geodatabase; Mobile Geodatabase (SQLite)  
- QGIS → PostGIS (spatial extension of PostgreSQL), SpatiaLite  

---

### Spatial Databases
- Designed for storing and managing **geographic data**
- Usually **relational** or **object-relational**
- Support spatial functions:
  - Measurement
  - Geoprocessing
  - Geometry operations
- Use **spatial indices** for efficient spatial queries:
  - BSP-tree
  - K-d tree
  - M-tree
  - R-tree (used by PostGIS)

> A spatial database is a **georeferenced spatial data system**.

---

## 2. The Modern Geospatial Data Stack (Late 2024)

DuckDB primarily operates in the **OLAP** layer of the modern geospatial data stack and integrates tightly with Python and modern analytical formats.

---

## 3. DuckDB Overview

DuckDB is:

- An **in-process database**
- No independent server process (similar to SQLite)
- Designed for **OLAP** workloads
- Reads CSV and Parquet directly
- Optimised for large analytical queries on a single machine

Official site: https://duckdb.org/

---

## 4. DuckDB as a Columnar OLAP Database

### Key Characteristics
- Row–columnar structure
- Data sliced into **row groups**
- Columns stored separately and compressed
- Similar to Parquet and ORC formats

---

## 5. Interoperable SQL-Powered DataFrames

DuckDB integrates seamlessly with:

- Pandas
- Polars
- NumPy
- Apache Arrow

### Capabilities
- SQL directly on DataFrames
- Zero-copy data exchange (via Arrow)
- High-performance analytical queries

---

## 6. DuckDB as a Federated Query Engine

DuckDB can query external systems including:

- PostgreSQL, MySQL
- JSON, CSV, Parquet files
- Amazon S3
- Apache Iceberg and Delta Lake

Supports persistent **read-only views** over external data.

---

## 7. DuckDB as a Single-Node Compute Engine

### Use cases
- Batch transformations
- CSV/JSON → Parquet pipelines
- Large aggregations on commodity hardware

Example: Aggregate 100M rows in ~1 minute.

---

## 8. DuckDB Spatial Extension

Built on mature geospatial libraries:

- GEOS
- GDAL / OGR
- PROJ

### Benefits
- SQL-based spatial analysis
- High-performance vectorised execution
- Import/export 50+ geospatial formats

⚠️ Still evolving; not fully OGC-compliant yet.

---

## 9. Why DuckDB Matters

> “The geospatial world needs to meet people more than halfway, enabling them to stay in their existing workflows and toolsets.”  
> — Chris Holmes (Planet, OGC, Radiant.Earth)

DuckDB bridges data science and databases with minimal infrastructure.

---

## 10. Useful Resources

- https://duckdb.org/
- https://duckdb.org/docs/
- https://motherduck.com/
- https://geog-414.gishub.org/book/duckdb/01_duckdb_intro.html
- https://github.com/davidgasquez/awesome-duckdb

---

## 11. Academic References

- DuckDB: an Embeddable Analytical Database (SIGMOD 2019)
- Data Management for Data Science (CIDR 2020)
- DuckDB-Wasm (VLDB 2022)
- Robust External Hash Aggregation (ICDE 2024)
- Runtime-Extensible Parsers (CIDR 2025)
