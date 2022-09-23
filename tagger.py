# coding=UTF-8
"""
Author: trickerer (https://github.com/trickerer, https://github.com/trickerer01)
"""
#########################################
#
#

from base64 import b64decode
from json import loads
from re import compile as re_compile, match as re_match, sub as re_sub
from typing import List, Dict

from defs import TAG_NUMS_ENCODED


TAG_NUMS_DECODED = loads(b64decode(TAG_NUMS_ENCODED))  # type: Dict[str, str]

re_replace_symbols = re_compile(
    r'[^0-9a-zA-Z_+()\[\]]+'
)

# used with re.sub
# noinspection RegExpAnonymousGroup
re_numbered_or_counted_tag = re_compile(
    r'^(?!rule_?\d+)(?:\d+?\+?)?([^\d]+?)(?:_\d+|s)?$'
)

re_tags_to_process = re_compile(
    r'^(?:.+?_warc.+?|(?:[a-z]+?_)?elf|drae.{3}|tent[a-z]{3}es|(?:bell[a-z]|sto[a-z]{4})_bul[a-z]{2,3}|inf[a-z]{5}n|egg(?:_[a-z]{3,9}|s)?|'
    r'[a-z]{4}hral_i.+?|(?:\d{1,2}\+?)?(?:boys?|girls?|fu[a-z]{2}(?:[a-z]{4}|s)?|in[d-v]{2}cts?)|succ[a-z]{4}|'
    r'bbw|dog|eel|f(?:acesitting|ur)|hmv|tar|c(?:\.c\.|um)|d\.va|na\'vi|kai\'sa|'
    r'[^(]+\([^)]+\).*?|[a-z_\-]+\d+?|\d{2,4}[a-z_\-]+?|[a-z_]{2,15}sfm|[^_]+_pov|fu[a-z]{2}(?:/|_(?:on|with)_)[a-z]{4}|'
    r'[a-z][a-z_]{3,8}|[a-g]ea?st[a-z]{6}|[lapymg]{3})$'
)

re_tags_exclude_major1 = re_compile(
    r'^(?:[234][dk]|h(?:d|ero_outfit)|level_up|p(?:ainting|rotagonist)|tagme|'
    r'war(?:rior|lock)|paladin|hunt(?:er|ress)|rogue|priest(?:ess)?|d(?:e(?:ath_?knight|mon_?hunt(?:er|ress))|ruid(?:ess)?)|'  # wow
    r'shaman|m(?:age|onk)|alliance|horde|'  # wow
    r'(?:human|orc|d(?:warf|raenei)|undead|forsaken|t(?:auren|roll)|g(?:nome|oblin)|worgen|pandaren)(?:_.+?)?|'  # wow
    r'[a-z]pose|[\da-z_\-]{14,}).*?$'
)
re_tags_exclude_major2 = re_compile(
    r'^(?:a(?:r(?:mor|twork)|udio)|cosplay|m(?:ap|eme|odel)|object|rwby|software|vtuber)$'
)

re_tags_to_not_exclude = re_compile(
    r'^(?:'
    r'a(?:liens?|m(?:azonium|b(?:er|rosine))|n(?:al|gel|imopron|thro)|r(?:achnid|iel))|'
    r'b(?:a(?:ndoned|tesz)|dsm|e(?:a(?:st|r)|n_10|wyx)|i(?:mbo|oshock|r(?:dway|th))|l(?:ack(?:ed)?|o(?:od|wjob))|o(?:dysuit|ndage|vine))|'
    r'c(?:a(?:ge|nine|t(?:_girl|woman))|entaur|hained|o(?:ot27|rset)|reampie|uckold)|'
    r'd(?:ark_elf|e(?:a(?:dpool|ath)|er|mons?|ntol|rpixon|zmall)|i(?:ablo|gimon|ldo)|mitrys|o(?:cking|gs?|nkey|om)|ragon(?:ess)?)|'
    r'e(?:ggs|lves|nema|quine|xtreme|zria)|'
    r'f(?:art(?:ing)?|e(?:m(?:boy|dom|shep)|ral)|isting|o(?:rtnite|x_girl)|rozen|u(?:rry|ta(?:holic|nari)))|'
    r'g(?:a(?:ngbang|p(?:e|ing))|i(?:ant(?:ess)?|fdoozer)|o(?:blins?|o_girl|re|th)|r(?:anny|eatb8)|u(?:il(?:mon|tyk)|robase))|'
    r'h(?:a(?:iry|l(?:f_elf|o)|ndjob)|e(?:lena|tero)|i(?:gh_elf|nca_p|ve)|o(?:ovesart|r(?:ror|se(?:_sex|girl)?)|usewife)|'
    r'rfidy|ulk|v54rdsl|ydrafxx)|'
    r'i(?:cedev|demi|n(?:c(?:est|ubus)|justice|sect(?:oid|s)?))|'
    r'j(?:a(?:ckerman|il)|uicyneko)|'
    r'k(?:a(?:madeva|sdaq|kami)|eycock|hajiit|idnapped|not(?:t(?:ed|ing))?|o(?:opa|rra)|reamu|udoart)|'
    r'l(?:a(?:osduude|tex)|e(?:ather|eterr|s(?:bian|dias))|o(?:op|punny))|'
    r'm(?:a(?:chine|g(?:ic|mallow)|id|jora|le(?:_(?:male|only)|sub)?)|ccree|e(?:klab|ltrib|ru|troid)|'
    r'i(?:dget|driff|ku|lf|n(?:ecraft|otaur|us8)|ruko|s(?:syb|tress))|o(?:nsters?|rty|xxy))|'
    r'n(?:aga|oih(?:_2)|ualia)|'
    r'o(?:gre|ne_piece|p(?:helia|iumud)|r(?:al|cs|gy)|verwatch)|'
    r'p(?:a(?:inful|ladins|ragon|uline)|ersona(?:_\d)?|i(?:kachu|ssing)|o(?:kemon|ny|wergirl)|pr(?:e(?:dator|gnant)|ison(?:er)?|olapse))|'
    r'r(?:a(?:d(?:eong3d|roach)|p(?:e|unzel)|tchet)|e(?:becca|dapple2|ey_art)|i(?:eklig|kolo)|u(?:bber|kia)|yona)|'
    r's(?:a(?:dako|itou|mira|ntalol|yuri)|ca(?:lie|t)|e(?:cazz?|lf_fuck)|hackles|i(?:lkymilk|ms(?:_\d)?|th_jedi)|k(?:arlet|yrim)|'
    r'l(?:ave|eepy_b|yxxx24)|mell|o(?:ft_vore|lo(?:_.+?)?|phi[ae]|r(?:aka|idormi))|p(?:i(?:der|troast|zzy)|l(?:atoon|ucky)|o(?:ks|nty))|'
    r't(?:a(?:lkek|r(?:_.+?|craft|fox))|ra(?:ight|pon)|udio34)|uccubus|ylveon)|'
    r't(?:a(?:ga|ker_pov)|e(?:kken|ntacles?|xelnaut)|he(?:_sims|count|hoaxxx)|ied|o(?:gruta|rture|uhou)|r(?:a(?:ns|ps?)|inity)|soni|'
    r'y(?:viania))|'
    r'u(?:g(?:ly(?:_man)?|oira)|n(?:birth|de(?:ad|rtale))|r(?:ethral|iel))|'
    r'v(?:a(?:lorant|mpire)|i(?:cer34|olence|rgin)|o(?:mit|re))|'
    r'w(?:ar(?:craft|frame|hammer)|hip)|'
    r'x(?:_(?:com(?:_\d)?|ray)|enomorph)|'
    r'z(?:o(?:mbies?|otopia))|'
    r'\d{1,2}\+?_?(?:animal|boy|futa|girl)s?.+?'  # 0-9
    r')$'
)


def validate_tag(tag: str) -> None:
    assert TAG_NUMS_DECODED.get(tag)


def trim_undersores(base_str: str) -> str:
    ret_str = re_sub(r'_{2,}', '_', base_str)
    if len(ret_str) != 0:
        if len(ret_str) >= 2 and ret_str[0] == '_' and ret_str[-1] == '_':
            ret_str = ret_str[1:-1]
        elif ret_str[-1] == '_':
            ret_str = ret_str[:-1]
        elif ret_str[0] == '_':
            ret_str = ret_str[1:]
    return ret_str


def filtered_tags(tags_list: List[str]) -> str:
    if len(tags_list) == 0:
        return ''

    tag_chars = '!abcdefghijklmnopqrstuvwxyz'
    tags_dict = {c: [] for c in tag_chars}  # type: Dict[str, List[str]]

    for tag in tags_list:
        tag = re_sub(re_replace_symbols, '_', tag)
        if re_match(re_tags_to_process, tag) is None:
            continue

        # digital_media_(artwork)
        aser_match = re_match(r'^([^(]+)\(([^)]+)\).*$', tag)
        aser_valid = False
        if aser_match:
            major_skip_match1 = re_match(re_tags_exclude_major1, aser_match.group(1))
            major_skip_match2 = re_match(re_tags_exclude_major2, aser_match.group(2))
            if major_skip_match1 or major_skip_match2:
                continue
            stag = trim_undersores(aser_match.group(1))
            if len(stag) >= 14:
                continue
            tag = stag
            aser_valid = True
        elif re_match(re_tags_to_not_exclude, tag) is None:
            continue

        tag = trim_undersores(tag)

        tag_char = tag[0] if tag[0] in tag_chars[1:] else tag_chars[0]
        do_add = True
        if len(tags_dict[tag_char]) > 0:
            # try and see
            # 1) if this tag can be consumed by existing tags
            # 2) if this tag can consume existing tags
            for i in reversed(range(len(tags_dict[tag_char]))):
                t = re_sub(re_numbered_or_counted_tag, r'\1', tags_dict[tag_char][i].lower())
                if len(t) >= len(tag) and (tag in t):
                    do_add = False
                    break
            if do_add:
                for i in reversed(range(len(tags_dict[tag_char]))):
                    t = re_sub(re_numbered_or_counted_tag, r'\1', tags_dict[tag_char][i].lower())
                    if len(tag) >= len(t) and (t in tag):
                        if aser_valid is False and tags_dict[tag_char][i][0].isupper():
                            aser_valid = True
                        del tags_dict[tag_char][i]
        if do_add:
            if aser_valid:
                for i, c in enumerate(tag):  # type: int, str
                    if (i == 0 or tag[i - 1] == '_') and c.isalpha():
                        tag = f'{tag[:i]}{c.upper()}{tag[i + 1:]}'
            tags_dict[tag_char].append(tag)

    tags_list_final = []
    [tags_list_final.extend(tag_list) for tag_list in sorted(tags_dict.values()) if len(tag_list) != 0]

    return trim_undersores("_".join(tags_list_final))

#
#
#########################################
