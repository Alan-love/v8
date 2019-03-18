# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  72: "EMPTY_STRING_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ASM_WASM_DATA_TYPE",
  159: "ASYNC_GENERATOR_REQUEST_TYPE",
  160: "CLASS_POSITIONS_TYPE",
  161: "DEBUG_INFO_TYPE",
  162: "FUNCTION_TEMPLATE_INFO_TYPE",
  163: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  164: "INTERCEPTOR_INFO_TYPE",
  165: "INTERPRETER_DATA_TYPE",
  166: "MODULE_INFO_ENTRY_TYPE",
  167: "MODULE_TYPE",
  168: "OBJECT_TEMPLATE_INFO_TYPE",
  169: "PROMISE_CAPABILITY_TYPE",
  170: "PROMISE_REACTION_TYPE",
  171: "PROTOTYPE_INFO_TYPE",
  172: "SCRIPT_TYPE",
  173: "STACK_FRAME_INFO_TYPE",
  174: "STACK_TRACE_FRAME_TYPE",
  175: "TUPLE2_TYPE",
  176: "TUPLE3_TYPE",
  177: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  178: "WASM_DEBUG_INFO_TYPE",
  179: "WASM_EXCEPTION_TAG_TYPE",
  180: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  181: "CALLABLE_TASK_TYPE",
  182: "CALLBACK_TASK_TYPE",
  183: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  184: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  185: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  186: "FINALIZATION_GROUP_CLEANUP_JOB_TASK_TYPE",
  187: "ALLOCATION_SITE_TYPE",
  188: "EMBEDDER_DATA_ARRAY_TYPE",
  189: "FIXED_ARRAY_TYPE",
  190: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  191: "HASH_TABLE_TYPE",
  192: "ORDERED_HASH_MAP_TYPE",
  193: "ORDERED_HASH_SET_TYPE",
  194: "ORDERED_NAME_DICTIONARY_TYPE",
  195: "NAME_DICTIONARY_TYPE",
  196: "GLOBAL_DICTIONARY_TYPE",
  197: "NUMBER_DICTIONARY_TYPE",
  198: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  199: "STRING_TABLE_TYPE",
  200: "EPHEMERON_HASH_TABLE_TYPE",
  201: "SCOPE_INFO_TYPE",
  202: "SCRIPT_CONTEXT_TABLE_TYPE",
  203: "AWAIT_CONTEXT_TYPE",
  204: "BLOCK_CONTEXT_TYPE",
  205: "CATCH_CONTEXT_TYPE",
  206: "DEBUG_EVALUATE_CONTEXT_TYPE",
  207: "EVAL_CONTEXT_TYPE",
  208: "FUNCTION_CONTEXT_TYPE",
  209: "MODULE_CONTEXT_TYPE",
  210: "NATIVE_CONTEXT_TYPE",
  211: "SCRIPT_CONTEXT_TYPE",
  212: "WITH_CONTEXT_TYPE",
  213: "WEAK_FIXED_ARRAY_TYPE",
  214: "TRANSITION_ARRAY_TYPE",
  215: "CALL_HANDLER_INFO_TYPE",
  216: "CELL_TYPE",
  217: "CODE_DATA_CONTAINER_TYPE",
  218: "DESCRIPTOR_ARRAY_TYPE",
  219: "FEEDBACK_CELL_TYPE",
  220: "FEEDBACK_VECTOR_TYPE",
  221: "LOAD_HANDLER_TYPE",
  222: "PREPARSE_DATA_TYPE",
  223: "PROPERTY_ARRAY_TYPE",
  224: "PROPERTY_CELL_TYPE",
  225: "SHARED_FUNCTION_INFO_TYPE",
  226: "SMALL_ORDERED_HASH_MAP_TYPE",
  227: "SMALL_ORDERED_HASH_SET_TYPE",
  228: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  229: "STORE_HANDLER_TYPE",
  230: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  231: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  232: "WEAK_ARRAY_LIST_TYPE",
  233: "WEAK_CELL_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_REF_TYPE",
  1082: "JS_FINALIZATION_GROUP_CLEANUP_ITERATOR_TYPE",
  1083: "JS_FINALIZATION_GROUP_TYPE",
  1084: "JS_WEAK_MAP_TYPE",
  1085: "JS_WEAK_SET_TYPE",
  1086: "JS_TYPED_ARRAY_TYPE",
  1087: "JS_DATA_VIEW_TYPE",
  1088: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1089: "JS_INTL_COLLATOR_TYPE",
  1090: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1091: "JS_INTL_LIST_FORMAT_TYPE",
  1092: "JS_INTL_LOCALE_TYPE",
  1093: "JS_INTL_NUMBER_FORMAT_TYPE",
  1094: "JS_INTL_PLURAL_RULES_TYPE",
  1095: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1096: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1097: "JS_INTL_SEGMENTER_TYPE",
  1098: "WASM_EXCEPTION_TYPE",
  1099: "WASM_GLOBAL_TYPE",
  1100: "WASM_INSTANCE_TYPE",
  1101: "WASM_MEMORY_TYPE",
  1102: "WASM_MODULE_TYPE",
  1103: "WASM_TABLE_TYPE",
  1104: "JS_BOUND_FUNCTION_TYPE",
  1105: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("RO_SPACE", 0x00139): (138, "FreeSpaceMap"),
  ("RO_SPACE", 0x00189): (132, "MetaMap"),
  ("RO_SPACE", 0x00209): (131, "NullMap"),
  ("RO_SPACE", 0x00271): (218, "DescriptorArrayMap"),
  ("RO_SPACE", 0x002d1): (213, "WeakFixedArrayMap"),
  ("RO_SPACE", 0x00321): (152, "OnePointerFillerMap"),
  ("RO_SPACE", 0x00371): (152, "TwoPointerFillerMap"),
  ("RO_SPACE", 0x003f1): (131, "UninitializedMap"),
  ("RO_SPACE", 0x00461): (8, "OneByteInternalizedStringMap"),
  ("RO_SPACE", 0x00501): (131, "UndefinedMap"),
  ("RO_SPACE", 0x00561): (129, "HeapNumberMap"),
  ("RO_SPACE", 0x005e1): (131, "TheHoleMap"),
  ("RO_SPACE", 0x00689): (131, "BooleanMap"),
  ("RO_SPACE", 0x00761): (72, "EmptyStringMap"),
  ("RO_SPACE", 0x007b1): (136, "ByteArrayMap"),
  ("RO_SPACE", 0x00801): (189, "FixedArrayMap"),
  ("RO_SPACE", 0x00851): (189, "FixedCOWArrayMap"),
  ("RO_SPACE", 0x008a1): (191, "HashTableMap"),
  ("RO_SPACE", 0x008f1): (128, "SymbolMap"),
  ("RO_SPACE", 0x00941): (40, "OneByteStringMap"),
  ("RO_SPACE", 0x00991): (201, "ScopeInfoMap"),
  ("RO_SPACE", 0x009e1): (225, "SharedFunctionInfoMap"),
  ("RO_SPACE", 0x00a31): (133, "CodeMap"),
  ("RO_SPACE", 0x00a81): (208, "FunctionContextMap"),
  ("RO_SPACE", 0x00ad1): (216, "CellMap"),
  ("RO_SPACE", 0x00b21): (224, "GlobalPropertyCellMap"),
  ("RO_SPACE", 0x00b71): (135, "ForeignMap"),
  ("RO_SPACE", 0x00bc1): (214, "TransitionArrayMap"),
  ("RO_SPACE", 0x00c11): (220, "FeedbackVectorMap"),
  ("RO_SPACE", 0x00cb1): (131, "ArgumentsMarkerMap"),
  ("RO_SPACE", 0x00d51): (131, "ExceptionMap"),
  ("RO_SPACE", 0x00df1): (131, "TerminationExceptionMap"),
  ("RO_SPACE", 0x00e99): (131, "OptimizedOutMap"),
  ("RO_SPACE", 0x00f39): (131, "StaleRegisterMap"),
  ("RO_SPACE", 0x00fa9): (210, "NativeContextMap"),
  ("RO_SPACE", 0x00ff9): (209, "ModuleContextMap"),
  ("RO_SPACE", 0x01049): (207, "EvalContextMap"),
  ("RO_SPACE", 0x01099): (211, "ScriptContextMap"),
  ("RO_SPACE", 0x010e9): (203, "AwaitContextMap"),
  ("RO_SPACE", 0x01139): (204, "BlockContextMap"),
  ("RO_SPACE", 0x01189): (205, "CatchContextMap"),
  ("RO_SPACE", 0x011d9): (212, "WithContextMap"),
  ("RO_SPACE", 0x01229): (206, "DebugEvaluateContextMap"),
  ("RO_SPACE", 0x01279): (202, "ScriptContextTableMap"),
  ("RO_SPACE", 0x012c9): (151, "FeedbackMetadataArrayMap"),
  ("RO_SPACE", 0x01319): (189, "ArrayListMap"),
  ("RO_SPACE", 0x01369): (130, "BigIntMap"),
  ("RO_SPACE", 0x013b9): (190, "ObjectBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x01409): (137, "BytecodeArrayMap"),
  ("RO_SPACE", 0x01459): (217, "CodeDataContainerMap"),
  ("RO_SPACE", 0x014a9): (150, "FixedDoubleArrayMap"),
  ("RO_SPACE", 0x014f9): (196, "GlobalDictionaryMap"),
  ("RO_SPACE", 0x01549): (219, "ManyClosuresCellMap"),
  ("RO_SPACE", 0x01599): (189, "ModuleInfoMap"),
  ("RO_SPACE", 0x015e9): (134, "MutableHeapNumberMap"),
  ("RO_SPACE", 0x01639): (195, "NameDictionaryMap"),
  ("RO_SPACE", 0x01689): (219, "NoClosuresCellMap"),
  ("RO_SPACE", 0x016d9): (197, "NumberDictionaryMap"),
  ("RO_SPACE", 0x01729): (219, "OneClosureCellMap"),
  ("RO_SPACE", 0x01779): (192, "OrderedHashMapMap"),
  ("RO_SPACE", 0x017c9): (193, "OrderedHashSetMap"),
  ("RO_SPACE", 0x01819): (194, "OrderedNameDictionaryMap"),
  ("RO_SPACE", 0x01869): (222, "PreparseDataMap"),
  ("RO_SPACE", 0x018b9): (223, "PropertyArrayMap"),
  ("RO_SPACE", 0x01909): (215, "SideEffectCallHandlerInfoMap"),
  ("RO_SPACE", 0x01959): (215, "SideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x019a9): (215, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x019f9): (198, "SimpleNumberDictionaryMap"),
  ("RO_SPACE", 0x01a49): (189, "SloppyArgumentsElementsMap"),
  ("RO_SPACE", 0x01a99): (226, "SmallOrderedHashMapMap"),
  ("RO_SPACE", 0x01ae9): (227, "SmallOrderedHashSetMap"),
  ("RO_SPACE", 0x01b39): (228, "SmallOrderedNameDictionaryMap"),
  ("RO_SPACE", 0x01b89): (199, "StringTableMap"),
  ("RO_SPACE", 0x01bd9): (230, "UncompiledDataWithoutPreparseDataMap"),
  ("RO_SPACE", 0x01c29): (231, "UncompiledDataWithPreparseDataMap"),
  ("RO_SPACE", 0x01c79): (232, "WeakArrayListMap"),
  ("RO_SPACE", 0x01cc9): (200, "EphemeronHashTableMap"),
  ("RO_SPACE", 0x01d19): (188, "EmbedderDataArrayMap"),
  ("RO_SPACE", 0x01d69): (233, "WeakCellMap"),
  ("RO_SPACE", 0x01db9): (58, "NativeSourceStringMap"),
  ("RO_SPACE", 0x01e09): (32, "StringMap"),
  ("RO_SPACE", 0x01e59): (41, "ConsOneByteStringMap"),
  ("RO_SPACE", 0x01ea9): (33, "ConsStringMap"),
  ("RO_SPACE", 0x01ef9): (45, "ThinOneByteStringMap"),
  ("RO_SPACE", 0x01f49): (37, "ThinStringMap"),
  ("RO_SPACE", 0x01f99): (35, "SlicedStringMap"),
  ("RO_SPACE", 0x01fe9): (43, "SlicedOneByteStringMap"),
  ("RO_SPACE", 0x02039): (34, "ExternalStringMap"),
  ("RO_SPACE", 0x02089): (42, "ExternalOneByteStringMap"),
  ("RO_SPACE", 0x020d9): (50, "UncachedExternalStringMap"),
  ("RO_SPACE", 0x02129): (0, "InternalizedStringMap"),
  ("RO_SPACE", 0x02179): (2, "ExternalInternalizedStringMap"),
  ("RO_SPACE", 0x021c9): (10, "ExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x02219): (18, "UncachedExternalInternalizedStringMap"),
  ("RO_SPACE", 0x02269): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x022b9): (58, "UncachedExternalOneByteStringMap"),
  ("RO_SPACE", 0x02309): (140, "FixedUint8ArrayMap"),
  ("RO_SPACE", 0x02359): (139, "FixedInt8ArrayMap"),
  ("RO_SPACE", 0x023a9): (142, "FixedUint16ArrayMap"),
  ("RO_SPACE", 0x023f9): (141, "FixedInt16ArrayMap"),
  ("RO_SPACE", 0x02449): (144, "FixedUint32ArrayMap"),
  ("RO_SPACE", 0x02499): (143, "FixedInt32ArrayMap"),
  ("RO_SPACE", 0x024e9): (145, "FixedFloat32ArrayMap"),
  ("RO_SPACE", 0x02539): (146, "FixedFloat64ArrayMap"),
  ("RO_SPACE", 0x02589): (147, "FixedUint8ClampedArrayMap"),
  ("RO_SPACE", 0x025d9): (149, "FixedBigUint64ArrayMap"),
  ("RO_SPACE", 0x02629): (148, "FixedBigInt64ArrayMap"),
  ("RO_SPACE", 0x02679): (131, "SelfReferenceMarkerMap"),
  ("RO_SPACE", 0x026e1): (175, "Tuple2Map"),
  ("RO_SPACE", 0x02781): (177, "ArrayBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x02ac1): (164, "InterceptorInfoMap"),
  ("RO_SPACE", 0x050a9): (153, "AccessCheckInfoMap"),
  ("RO_SPACE", 0x050f9): (154, "AccessorInfoMap"),
  ("RO_SPACE", 0x05149): (155, "AccessorPairMap"),
  ("RO_SPACE", 0x05199): (156, "AliasedArgumentsEntryMap"),
  ("RO_SPACE", 0x051e9): (157, "AllocationMementoMap"),
  ("RO_SPACE", 0x05239): (158, "AsmWasmDataMap"),
  ("RO_SPACE", 0x05289): (159, "AsyncGeneratorRequestMap"),
  ("RO_SPACE", 0x052d9): (160, "ClassPositionsMap"),
  ("RO_SPACE", 0x05329): (161, "DebugInfoMap"),
  ("RO_SPACE", 0x05379): (162, "FunctionTemplateInfoMap"),
  ("RO_SPACE", 0x053c9): (163, "FunctionTemplateRareDataMap"),
  ("RO_SPACE", 0x05419): (165, "InterpreterDataMap"),
  ("RO_SPACE", 0x05469): (166, "ModuleInfoEntryMap"),
  ("RO_SPACE", 0x054b9): (167, "ModuleMap"),
  ("RO_SPACE", 0x05509): (168, "ObjectTemplateInfoMap"),
  ("RO_SPACE", 0x05559): (169, "PromiseCapabilityMap"),
  ("RO_SPACE", 0x055a9): (170, "PromiseReactionMap"),
  ("RO_SPACE", 0x055f9): (171, "PrototypeInfoMap"),
  ("RO_SPACE", 0x05649): (172, "ScriptMap"),
  ("RO_SPACE", 0x05699): (173, "StackFrameInfoMap"),
  ("RO_SPACE", 0x056e9): (174, "StackTraceFrameMap"),
  ("RO_SPACE", 0x05739): (176, "Tuple3Map"),
  ("RO_SPACE", 0x05789): (178, "WasmDebugInfoMap"),
  ("RO_SPACE", 0x057d9): (179, "WasmExceptionTagMap"),
  ("RO_SPACE", 0x05829): (180, "WasmExportedFunctionDataMap"),
  ("RO_SPACE", 0x05879): (181, "CallableTaskMap"),
  ("RO_SPACE", 0x058c9): (182, "CallbackTaskMap"),
  ("RO_SPACE", 0x05919): (183, "PromiseFulfillReactionJobTaskMap"),
  ("RO_SPACE", 0x05969): (184, "PromiseRejectReactionJobTaskMap"),
  ("RO_SPACE", 0x059b9): (185, "PromiseResolveThenableJobTaskMap"),
  ("RO_SPACE", 0x05a09): (186, "FinalizationGroupCleanupJobTaskMap"),
  ("RO_SPACE", 0x05a59): (187, "AllocationSiteWithWeakNextMap"),
  ("RO_SPACE", 0x05aa9): (187, "AllocationSiteWithoutWeakNextMap"),
  ("RO_SPACE", 0x05af9): (221, "LoadHandler1Map"),
  ("RO_SPACE", 0x05b49): (221, "LoadHandler2Map"),
  ("RO_SPACE", 0x05b99): (221, "LoadHandler3Map"),
  ("RO_SPACE", 0x05be9): (229, "StoreHandler0Map"),
  ("RO_SPACE", 0x05c39): (229, "StoreHandler1Map"),
  ("RO_SPACE", 0x05c89): (229, "StoreHandler2Map"),
  ("RO_SPACE", 0x05cd9): (229, "StoreHandler3Map"),
  ("MAP_SPACE", 0x00139): (1057, "ExternalMap"),
  ("MAP_SPACE", 0x00189): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("RO_SPACE", 0x001d9): "NullValue",
  ("RO_SPACE", 0x00259): "EmptyDescriptorArray",
  ("RO_SPACE", 0x002c1): "EmptyWeakFixedArray",
  ("RO_SPACE", 0x003c1): "UninitializedValue",
  ("RO_SPACE", 0x004d1): "UndefinedValue",
  ("RO_SPACE", 0x00551): "NanValue",
  ("RO_SPACE", 0x005b1): "TheHoleValue",
  ("RO_SPACE", 0x00649): "HoleNanValue",
  ("RO_SPACE", 0x00659): "TrueValue",
  ("RO_SPACE", 0x00709): "FalseValue",
  ("RO_SPACE", 0x00751): "empty_string",
  ("RO_SPACE", 0x00c61): "EmptyScopeInfo",
  ("RO_SPACE", 0x00c71): "EmptyFixedArray",
  ("RO_SPACE", 0x00c81): "ArgumentsMarker",
  ("RO_SPACE", 0x00d21): "Exception",
  ("RO_SPACE", 0x00dc1): "TerminationException",
  ("RO_SPACE", 0x00e69): "OptimizedOut",
  ("RO_SPACE", 0x00f09): "StaleRegister",
  ("RO_SPACE", 0x026c9): "EmptyEnumCache",
  ("RO_SPACE", 0x02731): "EmptyPropertyArray",
  ("RO_SPACE", 0x02741): "EmptyByteArray",
  ("RO_SPACE", 0x02751): "EmptyObjectBoilerplateDescription",
  ("RO_SPACE", 0x02769): "EmptyArrayBoilerplateDescription",
  ("RO_SPACE", 0x027d1): "EmptyFixedUint8Array",
  ("RO_SPACE", 0x027f1): "EmptyFixedInt8Array",
  ("RO_SPACE", 0x02811): "EmptyFixedUint16Array",
  ("RO_SPACE", 0x02831): "EmptyFixedInt16Array",
  ("RO_SPACE", 0x02851): "EmptyFixedUint32Array",
  ("RO_SPACE", 0x02871): "EmptyFixedInt32Array",
  ("RO_SPACE", 0x02891): "EmptyFixedFloat32Array",
  ("RO_SPACE", 0x028b1): "EmptyFixedFloat64Array",
  ("RO_SPACE", 0x028d1): "EmptyFixedUint8ClampedArray",
  ("RO_SPACE", 0x028f1): "EmptyFixedBigUint64Array",
  ("RO_SPACE", 0x02911): "EmptyFixedBigInt64Array",
  ("RO_SPACE", 0x02931): "EmptySloppyArgumentsElements",
  ("RO_SPACE", 0x02951): "EmptySlowElementDictionary",
  ("RO_SPACE", 0x02999): "EmptyOrderedHashMap",
  ("RO_SPACE", 0x029c1): "EmptyOrderedHashSet",
  ("RO_SPACE", 0x029e9): "EmptyFeedbackMetadata",
  ("RO_SPACE", 0x029f9): "EmptyPropertyCell",
  ("RO_SPACE", 0x02a21): "EmptyPropertyDictionary",
  ("RO_SPACE", 0x02a71): "NoOpInterceptorInfo",
  ("RO_SPACE", 0x02b11): "EmptyWeakArrayList",
  ("RO_SPACE", 0x02b29): "InfinityValue",
  ("RO_SPACE", 0x02b39): "MinusZeroValue",
  ("RO_SPACE", 0x02b49): "MinusInfinityValue",
  ("RO_SPACE", 0x02b59): "SelfReferenceMarker",
  ("RO_SPACE", 0x02bb1): "OffHeapTrampolineRelocationInfo",
  ("RO_SPACE", 0x02bc9): "HashSeed",
  ("OLD_SPACE", 0x00139): "ArgumentsIteratorAccessor",
  ("OLD_SPACE", 0x001a9): "ArrayLengthAccessor",
  ("OLD_SPACE", 0x00219): "BoundFunctionLengthAccessor",
  ("OLD_SPACE", 0x00289): "BoundFunctionNameAccessor",
  ("OLD_SPACE", 0x002f9): "ErrorStackAccessor",
  ("OLD_SPACE", 0x00369): "FunctionArgumentsAccessor",
  ("OLD_SPACE", 0x003d9): "FunctionCallerAccessor",
  ("OLD_SPACE", 0x00449): "FunctionNameAccessor",
  ("OLD_SPACE", 0x004b9): "FunctionLengthAccessor",
  ("OLD_SPACE", 0x00529): "FunctionPrototypeAccessor",
  ("OLD_SPACE", 0x00599): "StringLengthAccessor",
  ("OLD_SPACE", 0x00609): "InvalidPrototypeValidityCell",
  ("OLD_SPACE", 0x00619): "EmptyScript",
  ("OLD_SPACE", 0x00699): "ManyClosuresCell",
  ("OLD_SPACE", 0x006a9): "ArrayConstructorProtector",
  ("OLD_SPACE", 0x006b9): "NoElementsProtector",
  ("OLD_SPACE", 0x006e1): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x006f1): "ArraySpeciesProtector",
  ("OLD_SPACE", 0x00719): "TypedArraySpeciesProtector",
  ("OLD_SPACE", 0x00741): "RegExpSpeciesProtector",
  ("OLD_SPACE", 0x00769): "PromiseSpeciesProtector",
  ("OLD_SPACE", 0x00791): "StringLengthProtector",
  ("OLD_SPACE", 0x007a1): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x007c9): "ArrayBufferDetachingProtector",
  ("OLD_SPACE", 0x007f1): "PromiseHookProtector",
  ("OLD_SPACE", 0x00819): "PromiseResolveProtector",
  ("OLD_SPACE", 0x00829): "MapIteratorProtector",
  ("OLD_SPACE", 0x00851): "PromiseThenProtector",
  ("OLD_SPACE", 0x00879): "SetIteratorProtector",
  ("OLD_SPACE", 0x008a1): "StringIteratorProtector",
  ("OLD_SPACE", 0x008c9): "SingleCharacterStringCache",
  ("OLD_SPACE", 0x010d9): "StringSplitCache",
  ("OLD_SPACE", 0x018e9): "RegExpMultipleCache",
  ("OLD_SPACE", 0x020f9): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
