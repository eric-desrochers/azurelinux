# ESRP Signing Investigation — AZL4 Beta PMC Publishing

Source: e-mail "FW: AZL4 Beta PMC publishing status" (Andrew Phelps → Pawel
Winogrodzki, 2026-05-05). The list below is the table extracted verbatim from
the section **"Specific list of RPMs that failed to sign:"**, followed by a
mapping of each failing RPM to the corresponding component definition in this
repository.

The signing failures are caused by malware-scan hits during ESRP signing of
AZL4 Alpha2 RPMs that are being published to PMC AZL4 Beta repos.

---

## Failed-signing table (from the e-mail)

| Alpha2 Repo | # Failed signing | RPM signing failures |
|---|---:|---|
| `base/x86_64` | 2 | `perl-Module-Signature-0.93-2.azl4~20260420.noarch.rpm`<br>`samba-winexe-4.23.5-1.azl4~20260420.x86_64.rpm` |
| `base/aarch64` | 3 | `llvm-static-21.1.8-1.azl4~20260420.aarch64.rpm`<br>`perl-Module-Signature-0.93-2.azl4~20260420.noarch.rpm`<br>`samba-winexe-4.23.5-1.azl4~20260420.aarch64.rpm` |
| `base/srpms` | 20 | `apache-commons-compress-1.27.1-1.azl4~20260420.src.rpm`<br>`chromium-145.0.7632.109-1.azl4~20260420.src.rpm`<br>`espeak-ng-1.51.1-12.azl4~20260420.src.rpm`<br>`exfatprogs-1.3.1-1.azl4~20260420.src.rpm`<br>`firefox-148.0-1.azl4~20260420.src.rpm`<br>`gdal-3.11.5-1.azl4~20260420.src.rpm`<br>`kf6-karchive-6.23.0-1.azl4~20260420.src.rpm`<br>`libabigail-2.9-1.azl4~20260420.src.rpm`<br>`libkml-1.3.0-56.azl4~20260420.src.rpm`<br>`mathjax-2.7.4-1.azl4~20260420.src.rpm`<br>`mozjs128-128.11.0-1.azl4~20260420.src.rpm`<br>`perl-Module-Signature-0.93-2.azl4~20260420.src.rpm`<br>`perl-Test-Signature-1.11-35.azl4~20260420.src.rpm`<br>`python-impacket-0.12.0-1.azl4~20260420.src.rpm`<br>`qt6-qtwebengine-6.10.2-1.azl4~20260420.src.rpm`<br>`rubygem-pdf-reader-2.4.2-10.azl4~20260420.src.rpm`<br>`star-1.6-18.azl4~20260420.src.rpm`<br>`stress-ng-0.20.01-1.azl4~20260420.src.rpm`<br>`texlive-2023-80.azl4~20260420.src.rpm`<br>`yara-4.5.4-1.azl4~20260420.src.rpm` |
| `base/debuginfo/x86_64` | 0 | None |
| `base/debuginfo/aarch64` | 0 | None |
| `sdk/x86_64` | 9 | `ghc-ghc-prof-9.8.4-149.azl4~20260420.x86_64.rpm`<br>`java-25-openjdk-portable-static-libs-slowdebug-25.0.0.0.32-0.1.ea.azl4~20260420.x86_64.rpm`<br>`java-25-openjdk-static-libs-slowdebug-25.0.0.0.32-0.3.ea.azl4~20260420.x86_64.rpm`<br>`llvm20-static-20.1.8-1.azl4~20260420.x86_64.rpm`<br>`mingw64-gettext-static-0.25.1-1.azl4~20260420.noarch.rpm`<br>`mingw64-libxml2-static-2.12.10-2.azl4~20260420.noarch.rpm`<br>`perl-Test-Signature-1.11-35.azl4~20260420.noarch.rpm`<br>`python3-impacket-0.12.0-1.azl4~20260420.noarch.rpm`<br>`qemu-tests-10.1.4-1.azl4~20260420.x86_64.rpm` |
| `sdk/aarch64` | 10 | `ghc-ghc-devel-9.8.4-149.azl4~20260420.aarch64.rpm`<br>`ghc-ghc-prof-9.8.4-149.azl4~20260420.aarch64.rpm`<br>`java-25-openjdk-portable-static-libs-slowdebug-25.0.0.0.32-0.1.ea.azl4~20260420.aarch64.rpm`<br>`java-25-openjdk-static-libs-slowdebug-25.0.0.0.32-0.3.ea.azl4~20260420.aarch64.rpm`<br>`llvm20-static-20.1.8-1.azl4~20260420.aarch64.rpm`<br>`mingw64-gettext-static-0.25.1-1.azl4~20260420.noarch.rpm`<br>`mingw64-libxml2-static-2.12.10-2.azl4~20260420.noarch.rpm`<br>`perl-Test-Signature-1.11-35.azl4~20260420.noarch.rpm`<br>`python3-impacket-0.12.0-1.azl4~20260420.noarch.rpm`<br>`qemu-tests-10.1.4-1.azl4~20260420.aarch64.rpm` |
| `sdk/srpms` | N/A | N/A |
| `sdk/debuginfo/x86_64` | 1 | `openfec-debuginfo-1.4.2.6-7.azl4~20260420.x86_64.rpm` |
| `sdk/debuginfo/aarch64` | 1 | `openfec-debuginfo-1.4.2.6-7.azl4~20260420.aarch64.rpm` |

---

## RPM → component mapping

Each failing RPM is mapped to the SRPM-level component (i.e. the spec file)
that produces it. Sub-packages and `-debuginfo` packages are mapped to their
parent spec. Versions in the rendered specs were verified to match the version
in each failing RPM.

| Failing RPM file name | Type | Component | Spec file | Notes |
|---|---|---|---|---|
| `apache-commons-compress-1.27.1-1.azl4~20260420.src.rpm` | SRPM | `apache-commons-compress` | [specs/a/apache-commons-compress/apache-commons-compress.spec](specs/a/apache-commons-compress/apache-commons-compress.spec) | Direct. |
| `espeak-ng-1.51.1-12.azl4~20260420.src.rpm` | SRPM | `espeak-ng` | [specs/e/espeak-ng/espeak-ng.spec](specs/e/espeak-ng/espeak-ng.spec) | Direct. |
| `exfatprogs-1.3.1-1.azl4~20260420.src.rpm` | SRPM | `exfatprogs` | [specs/e/exfatprogs/exfatprogs.spec](specs/e/exfatprogs/exfatprogs.spec) | Direct (Version 1.3.1). |
| `firefox-148.0-1.azl4~20260420.src.rpm` | SRPM | `firefox` | [specs/f/firefox/firefox.spec](specs/f/firefox/firefox.spec) | Direct (Version 148.0). |
| `gdal-3.11.5-1.azl4~20260420.src.rpm` | SRPM | `gdal` | [specs/g/gdal/gdal.spec](specs/g/gdal/gdal.spec) | Direct (Version 3.11.5). |
| `ghc-ghc-devel-9.8.4-149.azl4~20260420.aarch64.rpm` | binary subpackage | `ghc` | [specs/g/ghc/ghc.spec](specs/g/ghc/ghc.spec) | Subpackage `ghc-ghc-devel`; same SRPM as `ghc-ghc-prof`. |
| `ghc-ghc-prof-9.8.4-149.azl4~20260420.aarch64.rpm` | binary subpackage | `ghc` | [specs/g/ghc/ghc.spec](specs/g/ghc/ghc.spec) | aarch64 build of the `ghc-ghc-prof` subpackage; `Version: 9.8.4` matches. |
| `ghc-ghc-prof-9.8.4-149.azl4~20260420.x86_64.rpm` | binary subpackage | `ghc` | [specs/g/ghc/ghc.spec](specs/g/ghc/ghc.spec) | x86_64 build of the `ghc-ghc-prof` subpackage (the GHC compiler library's profiling artefacts); `Version: 9.8.4` matches. |
| `java-25-openjdk-static-libs-slowdebug-25.0.0.0.32-0.3.ea.azl4~20260420.aarch64.rpm` | binary subpackage | `java-25-openjdk` | [specs/j/java-25-openjdk/java-25-openjdk.spec](specs/j/java-25-openjdk/java-25-openjdk.spec) | aarch64 build of the "slowdebug" `static-libs` subpackage of the OpenJDK 25 EA build. |
| `java-25-openjdk-static-libs-slowdebug-25.0.0.0.32-0.3.ea.azl4~20260420.x86_64.rpm` | binary subpackage | `java-25-openjdk` | [specs/j/java-25-openjdk/java-25-openjdk.spec](specs/j/java-25-openjdk/java-25-openjdk.spec) | x86_64 build of the "slowdebug" `static-libs` subpackage of the OpenJDK 25 EA build. |
| `java-25-openjdk-portable-static-libs-slowdebug-25.0.0.0.32-0.1.ea.azl4~20260420.aarch64.rpm` | binary subpackage | `java-25-openjdk-portable` | [specs/j/java-25-openjdk-portable/java-25-openjdk-portable.spec](specs/j/java-25-openjdk-portable/java-25-openjdk-portable.spec) | aarch64 build of the "slowdebug" `static-libs` subpackage of the OpenJDK 25 EA "portable" variant SRPM. |
| `java-25-openjdk-portable-static-libs-slowdebug-25.0.0.0.32-0.1.ea.azl4~20260420.x86_64.rpm` | binary subpackage | `java-25-openjdk-portable` | [specs/j/java-25-openjdk-portable/java-25-openjdk-portable.spec](specs/j/java-25-openjdk-portable/java-25-openjdk-portable.spec) | x86_64 build of the "slowdebug" `static-libs` subpackage of the OpenJDK 25 EA "portable" variant SRPM. |
| `kf6-karchive-6.23.0-1.azl4~20260420.src.rpm` | SRPM | `kf6-karchive` | [specs/k/kf6-karchive/kf6-karchive.spec](specs/k/kf6-karchive/kf6-karchive.spec) | Direct. |
| `libabigail-2.9-1.azl4~20260420.src.rpm` | SRPM | `libabigail` | [specs/l/libabigail/libabigail.spec](specs/l/libabigail/libabigail.spec) | Direct. |
| `libkml-1.3.0-56.azl4~20260420.src.rpm` | SRPM | `libkml` | [specs/l/libkml/libkml.spec](specs/l/libkml/libkml.spec) | Direct. |
| `llvm-static-21.1.8-1.azl4~20260420.aarch64.rpm` | binary subpackage | `llvm` | [specs/l/llvm/llvm.spec](specs/l/llvm/llvm.spec) | `%global maj_ver 21 / min_ver 1 / patch_ver 8`; main build → `pkg_name_llvm = llvm`, so subpackage is `llvm-static`. |
| `llvm20-static-20.1.8-1.azl4~20260420.aarch64.rpm` | binary subpackage | `llvm20` | [specs/l/llvm20/llvm20.spec](specs/l/llvm20/llvm20.spec) | aarch64 build; compat build (`pkg_name_llvm = llvm%{maj_ver}` = `llvm20` → subpackage `llvm20-static`). `maj/min/patch = 20/1/8`. |
| `llvm20-static-20.1.8-1.azl4~20260420.x86_64.rpm` | binary subpackage | `llvm20` | [specs/l/llvm20/llvm20.spec](specs/l/llvm20/llvm20.spec) | x86_64 build; compat build (`pkg_name_llvm = llvm%{maj_ver}` = `llvm20` → subpackage `llvm20-static`). `maj/min/patch = 20/1/8`. |
| `mathjax-2.7.4-1.azl4~20260420.src.rpm` | SRPM | `mathjax` | [specs/m/mathjax/mathjax.spec](specs/m/mathjax/mathjax.spec) | Direct (Version 2.7.4). |
| `mingw64-gettext-static-0.25.1-1.azl4~20260420.noarch.rpm` | binary subpackage | `mingw-gettext` | [specs/m/mingw-gettext/mingw-gettext.spec](specs/m/mingw-gettext/mingw-gettext.spec) | `%package -n mingw64-gettext-static`. Listed under both `sdk/x86_64` and `sdk/aarch64` (same `noarch` RPM). |
| `mingw64-libxml2-static-2.12.10-2.azl4~20260420.noarch.rpm` | binary subpackage | `mingw-libxml2` | [specs/m/mingw-libxml2/mingw-libxml2.spec](specs/m/mingw-libxml2/mingw-libxml2.spec) | `%package -n mingw64-libxml2-static`; `Version: 2.12.10`. Listed under both `sdk/x86_64` and `sdk/aarch64` (same `noarch` RPM). |
| `mozjs128-128.11.0-1.azl4~20260420.src.rpm` | SRPM | `mozjs128` | [specs/m/mozjs128/mozjs128.spec](specs/m/mozjs128/mozjs128.spec) | Direct (Version 128.11.0). |
| `openfec-debuginfo-1.4.2.6-7.azl4~20260420.aarch64.rpm` | auto-generated debuginfo | `openfec` | [specs/o/openfec/openfec.spec](specs/o/openfec/openfec.spec) | aarch64 build. Standard `*-debuginfo` produced by rpmbuild from the `openfec` SRPM. |
| `openfec-debuginfo-1.4.2.6-7.azl4~20260420.x86_64.rpm` | auto-generated debuginfo | `openfec` | [specs/o/openfec/openfec.spec](specs/o/openfec/openfec.spec) | x86_64 build. Standard `*-debuginfo` produced by rpmbuild from the `openfec` SRPM. |
| `perl-Module-Signature-0.93-2.azl4~20260420.noarch.rpm` | binary (`noarch`) | `perl-Module-Signature` | [specs/p/perl-Module-Signature/perl-Module-Signature.spec](specs/p/perl-Module-Signature/perl-Module-Signature.spec) | Listed under both `base/x86_64` and `base/aarch64` (same `noarch` RPM). |
| `perl-Module-Signature-0.93-2.azl4~20260420.src.rpm` | SRPM | `perl-Module-Signature` | [specs/p/perl-Module-Signature/perl-Module-Signature.spec](specs/p/perl-Module-Signature/perl-Module-Signature.spec) | SRPM that produces the `noarch` binary above. |
| `perl-Test-Signature-1.11-35.azl4~20260420.noarch.rpm` | binary (`noarch`) | `perl-Test-Signature` | [specs/p/perl-Test-Signature/perl-Test-Signature.spec](specs/p/perl-Test-Signature/perl-Test-Signature.spec) | Listed under both `sdk/x86_64` and `sdk/aarch64` (same `noarch` RPM). |
| `perl-Test-Signature-1.11-35.azl4~20260420.src.rpm` | SRPM | `perl-Test-Signature` | [specs/p/perl-Test-Signature/perl-Test-Signature.spec](specs/p/perl-Test-Signature/perl-Test-Signature.spec) | SRPM that produces the `noarch` binary above. |
| `python-impacket-0.12.0-1.azl4~20260420.src.rpm` | SRPM | `python-impacket` | [specs/p/python-impacket/python-impacket.spec](specs/p/python-impacket/python-impacket.spec) | Direct (Version 0.12.0). |
| `python3-impacket-0.12.0-1.azl4~20260420.noarch.rpm` | binary subpackage | `python-impacket` | [specs/p/python-impacket/python-impacket.spec](specs/p/python-impacket/python-impacket.spec) | Generated as `python3-impacket` from the `python-impacket` SRPM. Listed under both `sdk/x86_64` and `sdk/aarch64` (same `noarch` RPM). |
| `qemu-tests-10.1.4-1.azl4~20260420.aarch64.rpm` | binary subpackage | `qemu` | [specs/q/qemu/qemu.spec](specs/q/qemu/qemu.spec) | aarch64 build of the `qemu-tests` subpackage; `Version: 10.1.4`. |
| `qemu-tests-10.1.4-1.azl4~20260420.x86_64.rpm` | binary subpackage | `qemu` | [specs/q/qemu/qemu.spec](specs/q/qemu/qemu.spec) | x86_64 build of `%package tests`; `Version: 10.1.4`. Likely scanner trigger: the qemu test suite ships intentionally-malformed binaries / firmware blobs used as fuzzer fixtures. |
| `qt6-qtwebengine-6.10.2-1.azl4~20260420.src.rpm` | SRPM | `qt6-qtwebengine` | [specs/q/qt6-qtwebengine/qt6-qtwebengine.spec](specs/q/qt6-qtwebengine/qt6-qtwebengine.spec) | Direct (Version 6.10.2). Note: bundles a Chromium tree internally — likely the same scanner trigger as `chromium`. |
| `rubygem-pdf-reader-2.4.2-10.azl4~20260420.src.rpm` | SRPM | `rubygem-pdf-reader` | [specs/r/rubygem-pdf-reader/rubygem-pdf-reader.spec](specs/r/rubygem-pdf-reader/rubygem-pdf-reader.spec) | Direct. |
| `samba-winexe-4.23.5-1.azl4~20260420.aarch64.rpm` | binary subpackage | `samba` | [specs/s/samba/samba.spec](specs/s/samba/samba.spec) | aarch64 build of `samba-winexe`; same spec as the x86_64 entry. |
| `samba-winexe-4.23.5-1.azl4~20260420.x86_64.rpm` | binary subpackage | `samba` | [specs/s/samba/samba.spec](specs/s/samba/samba.spec) | x86_64 build of `samba-winexe`. `%package winexe` gated by `%bcond winexe 1`; `%global samba_version 4.23.5` matches. |
| `star-1.6-18.azl4~20260420.src.rpm` | SRPM | `star` | [specs/s/star/star.spec](specs/s/star/star.spec) | Direct. |
| `stress-ng-0.20.01-1.azl4~20260420.src.rpm` | SRPM | `stress-ng` | [specs/s/stress-ng/stress-ng.spec](specs/s/stress-ng/stress-ng.spec) | Direct (Version 0.20.01). |
| `texlive-2023-80.azl4~20260420.src.rpm` | SRPM | `texlive` | [specs/t/texlive/texlive.spec](specs/t/texlive/texlive.spec) | `%global tl_version 2023`; `Version: %{tl_version}` → "2023". |
| `yara-4.5.4-1.azl4~20260420.src.rpm` | SRPM | `yara` | [specs/y/yara/yara.spec](specs/y/yara/yara.spec) | Direct (Version 4.5.4). Likely scanner self-recognition: YARA ships malware-rule fixtures in its test corpus. |
| `chromium-145.0.7632.109-1.azl4~20260420.src.rpm` | SRPM | **(none — not in this repo)** | — | **Cannot map.** No `chromium` component or spec exists in this repo. The comment in [base/comps/rubygem-railties/rubygem-railties.comp.toml](base/comps/rubygem-railties/rubygem-railties.comp.toml) explicitly states: *"Chromium/chromedriver are not available in Azure Linux"*. The SRPM in the AZL4 Alpha2 repo therefore must originate from an upstream / external source (e.g. a Fedora rebuild ingested into the publish flow), not from this `azurelinux` repo. **This needs follow-up with the publishing pipeline owners** to confirm where this SRPM is produced. Sorted to the end of the table since there is no component name to alphabetise on. |

---

## Summary by component

The **31 unique failing RPMs** (collapsing duplicates across architectures and
between `base/*` & `base/srpms`) map to **29 distinct components** in this
repo, plus **1 RPM (`chromium`) that does not map to any component** here.

Components affected (sorted):

1. `apache-commons-compress`
2. `espeak-ng`
3. `exfatprogs`
4. `firefox`
5. `gdal`
6. `ghc`
7. `java-25-openjdk`
8. `java-25-openjdk-portable`
9. `kf6-karchive`
10. `libabigail`
11. `libkml`
12. `llvm`
13. `llvm20`
14. `mathjax`
15. `mingw-gettext`
16. `mingw-libxml2`
17. `mozjs128`
18. `openfec`
19. `perl-Module-Signature`
20. `perl-Test-Signature`
21. `python-impacket`
22. `qemu`
23. `qt6-qtwebengine`
24. `rubygem-pdf-reader`
25. `samba`
26. `star`
27. `stress-ng`
28. `texlive`
29. `yara`

(29 entries — `java-25-openjdk` and `java-25-openjdk-portable` are listed
separately because they are independent SRPMs; `python-impacket` covers both
the SRPM and the `python3-impacket` binary subpackage; `llvm` and `llvm20` are
separate component SRPMs.)

## Unmapped RPMs

| RPM | Reason |
|---|---|
| `chromium-145.0.7632.109-1.azl4~20260420.src.rpm` | No `chromium` spec or component exists in this repository (`grep` over `base/comps/**/*.toml` and `specs/**/*.spec` returns nothing). The repo explicitly notes Chromium is not packaged in Azure Linux (see [base/comps/rubygem-railties/rubygem-railties.comp.toml](base/comps/rubygem-railties/rubygem-railties.comp.toml)). The SRPM listed in the AZL4 Alpha2 publishing flow must therefore come from an external source (e.g. an upstream Fedora rebuild that is ingested into the AZL4 publishing pipeline outside of this repo). Follow up with the publishing pipeline owners to identify the source repository. |

## Notes / observations for triage

- Many of the failures are highly plausible **false positives from the malware
  scanner**:
  - `yara` ships its own test corpus of malware-detection fixtures.
  - `qemu-tests` ships intentionally-malformed firmware/binaries used as
    fuzzer fixtures.
  - `qt6-qtwebengine` and `firefox` bundle a full Chromium tree internally and
    contain large blobs of obfuscated/optimised JS that frequently trip
    heuristic engines (this is consistent with `chromium` itself failing).
  - `mozjs128` (the SpiderMonkey JavaScript engine used by Firefox) — same
    family of triggers as Firefox/Chromium.
  - `perl-Module-Signature` / `perl-Test-Signature` — packages whose entire
    purpose is to verify cryptographic signatures; their test data may include
    deliberately-malformed signed payloads.
  - `samba-winexe` ships a precompiled Windows PE binary
    (`/usr/bin/winexe.exe`) used to launch commands on remote Windows hosts
    via SMB — this is exactly the kind of artefact AV engines flag as a
    hack-tool / "remote command execution utility" (see also `python-impacket`
    / `python3-impacket`, which is the canonical Python SMB/MSRPC toolkit
    used by red-team tools).
  - `*-static` packages (`llvm-static`, `llvm20-static`,
    `mingw64-gettext-static`, `mingw64-libxml2-static`,
    `java-25-*-static-libs-slowdebug`, `ghc-ghc-prof`) ship large static
    archives whose contents heuristic scanners often misclassify.
  - `mathjax` is JavaScript bundles; `texlive`, `kf6-karchive`,
    `apache-commons-compress`, `rubygem-pdf-reader`, `libkml`, `gdal`,
    `libabigail`, `espeak-ng`, `exfatprogs`, `star`, `stress-ng` — these are
    less obvious; would need the actual scanner's `virus_to_srpm_matches`
    spreadsheet (linked in the source e-mail) to triage individually.

- **Next step**: cross-reference this list against the
  `virus_to_srpm_matches-partial.xlsx` attachment referenced at the bottom of
  the source e-mail to get the specific virus-name → file-path matches per
  SRPM, then decide for each whether to (a) request a scanner allow-list /
  exception, (b) strip the offending fixture/blob via an overlay, or (c)
  exclude the affected sub-package from publishing.
