import os
from pathlib import Path

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
)
from text_renderer.layout.same_line import SameLineLayout
from text_renderer.layout.extra_text_line import ExtraTextLineLayout


CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = CURRENT_DIR / "output"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
CHAR_DIR = DATA_DIR / "char"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text"

font_cfg = dict(
    font_dir=FONT_DIR,
    font_list_file=FONT_LIST_DIR / "font_list.txt",
    font_size=(30, 31),
)

perspective_transform = NormPerspectiveTransformCfg(5, 5, 1.5)

chn_data = GeneratorCfg(
    num_image=50,
    save_dir=OUT_DIR / "char_corpus",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=CharCorpus(
            CharCorpusCfg(
                text_paths=[TEXT_DIR / "chn_text.txt", TEXT_DIR / "eng_text.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "chn.txt",
                length=(5, 10),
                char_spacing=(-0.3, 1.3),
                **font_cfg
            ),
        ),
        corpus_effects=Effects([Line(0.5), OneOf([DropoutRand(), DropoutVertical()])]),
    ),
)


enum_data = GeneratorCfg(
    num_image=50,
    save_dir=OUT_DIR / "enum_corpus",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "enum_text.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "chn.txt",
                **font_cfg
            ),
        ),
    ),
)

rand_data = GeneratorCfg(
    num_image=50,
    save_dir=OUT_DIR / "rand_corpus",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=RandCorpus(RandCorpusCfg(chars_file=CHAR_DIR / "chn.txt", **font_cfg),),
    ),
)

eng_word_data = GeneratorCfg(
    num_image=2000000,
    save_dir=OUT_DIR / "word_corpus",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "twitter_en_big.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "eng.txt",
                num_word = (3,10),
                **font_cfg
            ),
        ),
    ),
)


same_line_data = GeneratorCfg(
    num_image=100,
    save_dir=OUT_DIR / "same_line_data",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=SameLineLayout(),
        gray=False,
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[TEXT_DIR / "enum_text.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "chn.txt",
                    **font_cfg
                ),
            ),
            CharCorpus(
                CharCorpusCfg(
                    text_paths=[TEXT_DIR / "chn_text.txt", TEXT_DIR / "eng_text.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "chn.txt",
                    length=(5, 10),
                    font_dir=font_cfg["font_dir"],
                    font_list_file=font_cfg["font_list_file"],
                    font_size=(30, 35),
                ),
            ),
        ],
        corpus_effects=[Effects([Padding(), DropoutRand()]), NoEffects(),],
        layout_effects=Effects(Line(p=1)),
    ),
)


extra_text_line_data = GeneratorCfg(
    num_image=100,
    save_dir=OUT_DIR / "extra_text_line_data",
    render_cfg=RenderCfg(
        bg_dir=BG_DIR,
        perspective_transform=perspective_transform,
        layout=ExtraTextLineLayout(),
        corpus=[
            CharCorpus(
                CharCorpusCfg(
                    text_paths=[TEXT_DIR / "chn_text.txt", TEXT_DIR / "eng_text.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "chn.txt",
                    length=(9, 10),
                    font_dir=font_cfg["font_dir"],
                    font_list_file=font_cfg["font_list_file"],
                    font_size=(30, 35),
                ),
            ),
            CharCorpus(
                CharCorpusCfg(
                    text_paths=[TEXT_DIR / "chn_text.txt", TEXT_DIR / "eng_text.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "chn.txt",
                    length=(9, 10),
                    font_dir=font_cfg["font_dir"],
                    font_list_file=font_cfg["font_list_file"],
                    font_size=(30, 35),
                ),
            ),
        ],
        corpus_effects=[Effects([Padding()]), NoEffects()],
        layout_effects=Effects(Line(p=1)),
    ),
)

configs = [
    eng_word_data
]

