# My GraphIt Codes

Bucketing is generally used to exploit parallelism and maintain ordering in ordered graph algorithms.
It is expressive enough to implement many parallel ordered
graph algorithms. Existing frameworks support either lazy bucket update or eager bucket update approach.
Bucketing data structure is used to maintain the execution ordering. Each bucket
stores active vertices of the same priority, and the buckets are sorted in priority order. The program processes one
bucket at a time in priority order and dynamically moves
active vertices to new buckets when their priorities change.
Updates to the bucket structure can be implemented using
either an eager bucket update  approach or a lazy bucket
update approach.


GraphIt decouples the algorithm from optimizations for unordered graph algorithms.
