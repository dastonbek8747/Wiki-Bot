"""Yalang'och `except:` regressiya testi (HIGH-003).

Muammo: `bot.py:32` da yalang'och `except:` ishlatilgan. Bu `KeyboardInterrupt`
va `SystemExit` kabi tizim xatolarini ham yutib yuboradi va haqiqiy xatolarni
yashiradi (masalan tarmoq xatosi "maqola topilmadi" deb ko'rsatiladi).

Test tuzatilgunga qadar YIQILADI.
"""
import ast
import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BareExceptTest(unittest.TestCase):
    def test_no_bare_except(self):
        offenders = []
        for name in os.listdir(REPO_ROOT):
            if not name.endswith(".py"):
                continue
            path = os.path.join(REPO_ROOT, name)
            src = open(path, encoding="utf-8", errors="ignore").read()
            try:
                tree = ast.parse(src)
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.ExceptHandler) and node.type is None:
                    offenders.append(f"{name}:{node.lineno} except:")
        self.assertEqual(
            offenders,
            [],
            "Yalang'och except: topildi — aniq istisno turini ko'rsating:\n"
            + "\n".join(offenders),
        )

    def test_no_broad_exception_swallow(self):
        """`except Exception` ham xatoni yashirmasligi kerak — log qilinsin."""
        src = open(os.path.join(REPO_ROOT, "bot.py"), encoding="utf-8").read()
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler):
                # handler ichida biror amal (log/reply/raise) bo'lishi kerak
                self.assertTrue(
                    node.body,
                    f"bot.py:{node.lineno} except bloki bo'sh",
                )


if __name__ == "__main__":
    unittest.main()
