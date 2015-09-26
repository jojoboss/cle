from . import generic

arch = 'ARM'

R_ARM_COPY = generic.GenericCopyReloc
R_ARM_GLOB_DAT = generic.GenericJumpslotReloc
R_ARM_JUMP_SLOT = generic.GenericJumpslotReloc
R_ARM_RELATIVE = generic.GenericRelativeReloc

R_ARM_TLS_DTPMOD32 = generic.GenericTLSModIdReloc
R_ARM_TLS_DTPOFF32 = generic.GenericTLSDoffsetReloc
R_ARM_TLS_TPOFF32 = generic.GenericTLSOffsetReloc
