find_library(GPSTK_LIBRARY
  NAMES gpstk
  )
find_path(GPSTK_INCLUDE_DIR
  ConfDataReader.hpp 
  PATH_SUFFIXES gpstk )

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(GPStk DEFAULT_MSG GPSTK_LIBRARY GPSTK_INCLUDE_DIR)

mark_as_advanced(
  GPSTK_INCLUDE_DIR
  GPSTK_LIBRARY )

set(GPSTK_LIBRARIES ${GPSTK_LIBRARY} )
set(GPSTK_INCLUDE_DIRS ${GPSTK_INCLUDE_DIR} )

#======================
