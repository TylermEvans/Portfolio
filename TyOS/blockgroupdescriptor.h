#pragma once
#pragma pack(push,1)
struct BlockGroupDescriptor{
    unsigned block_bitmap;
    unsigned inode_bitmap;
    unsigned inode_table;
    unsigned short free_blocks;
    unsigned short free_inodes;
    unsigned short used_dirs;
    unsigned short pad;
    char reserved[12];
};
#pragma pack(pop)