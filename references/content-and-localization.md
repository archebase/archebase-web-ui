# Content and localization

ArcheBase interfaces may combine Chinese and Latin text. Treat language as a
layout input, not a late copy edit.

## Before implementation

- identify the primary language and whether bilingual fallback is required;
- record approved public naming and terminology from the strategy/VI layers;
- reserve width for the longest supplied variant, not the shortest translation;
- decide how metrics, units, dates, code, acronyms and product names are formatted;
- keep source/date/claim labels close to the claim they qualify.

## Mixed-script checks

- verify Chinese and Latin fonts render with the intended weight and baseline;
- test Chinese title wrapping at every target viewport;
- avoid fixed heights for text containers unless overflow behavior is defined;
- do not insert English-only punctuation rules into Chinese copy without a reason;
- test buttons, tabs, nav labels and error messages with the longest translation;
- keep semantic order correct when visual order changes on mobile.
