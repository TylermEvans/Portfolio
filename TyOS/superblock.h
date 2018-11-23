#pragma once
#pragma pack(push,1)
struct Superblock{
    unsigned inode_count;
    unsigned block_count;
    unsigned r_block_count;
    unsigned free_block_count;
    unsigned free_inode_count;
    unsigned first_data_block;
    unsigned logical_block_size;
    unsigned logical_fragment_size;
    unsigned blocks_per_group;
    unsigned fragments_per_group;
    unsigned inodes_per_group;
    unsigned mounttime; 
    unsigned writetime;
    unsigned short mountcount;
    unsigned short maxmountcount;
    unsigned short magic;
    unsigned short state;
    unsigned short errors;
    unsigned short minorrev;
    unsigned lastcheck;
    unsigned checktime;
    unsigned creator;
    unsigned revision;
    unsigned short resuid;
    unsigned short resgid;
    unsigned first_inode;
    unsigned short inode_size;
    unsigned short block_group_number;
    unsigned feature_compat;
    unsigned feature_incompat;
    unsigned feature_ro_compat;
    unsigned char uuid[16];
    char volname[16];
    char lastmount[64];
    char reserved[824];
};
#pragma pack(pop)