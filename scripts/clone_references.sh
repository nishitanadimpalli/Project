#!/usr/bin/env bash
set -euo pipefail
mkdir -p references
# Clone calculator project and python_super_course_source into references
if [ ! -d references/code_quality_calc ]; then
  git clone https://github.com/kaw393939/code_quality_calc.git references/code_quality_calc
else
  echo "references/code_quality_calc already exists, skipping clone"
fi
if [ ! -d references/python_super_course_source ]; then
  git clone https://github.com/kaw393939/python_super_course_source.git references/python_super_course_source
else
  echo "references/python_super_course_source already exists, skipping clone"
fi
printf "Cloned/verified repos in references/\n"
