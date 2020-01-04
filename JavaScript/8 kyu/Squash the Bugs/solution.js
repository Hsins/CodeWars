// [8 kyu] Squash the bugs
//
// Author:   Hsins
// Date:     2020/01/04

const findLongest = string => Math.max(...string.split(' ').map(x => x.length));
