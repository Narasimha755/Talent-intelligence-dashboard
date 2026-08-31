Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
using System.Text;

public class CredHelperFinal {
    [DllImport("advapi32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
    public static extern bool CredRead(string target, int type, int reservedFlag, out IntPtr credentialPtr);

    [DllImport("advapi32.dll", SetLastError = true)]
    public static extern void CredFree(IntPtr cred);

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    public struct CREDENTIAL {
        public int Flags;
        public int Type;
        public string TargetName;
        public string Comment;
        public long LastWritten;
        public int CredentialBlobSize;
        public IntPtr CredentialBlob;
        public int Persist;
        public int AttributeCount;
        public IntPtr Attributes;
        public string TargetAlias;
        public string UserName;
    }

    public static string ReadCredUtf8(string target) {
        IntPtr credPtr;
        if (CredRead(target, 1, 0, out credPtr)) {
            CREDENTIAL cred = (CREDENTIAL)Marshal.PtrToStructure(credPtr, typeof(CREDENTIAL));
            byte[] bytes = new byte[cred.CredentialBlobSize];
            Marshal.Copy(cred.CredentialBlob, bytes, 0, cred.CredentialBlobSize);
            CredFree(credPtr);
            return Encoding.UTF8.GetString(bytes);
        }
        return null;
    }
}
"@

$token = [CredHelperFinal]::ReadCredUtf8("GitHub - https://api.github.com/Narasimha755")
if (-not $token) {
    Write-Error "Could not retrieve token from Windows Credential Manager."
    exit 1
}

Write-Host "Authenticating as Narasimha755 with retrieved token..."
$remoteUrl = "https://Narasimha755:$token@github.com/Narasimha755/Talent-intelligence-dashboard.git"

# Push to main
git push --force $remoteUrl main:main
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ SUCCESS: All commits pushed successfully to origin/main!"
} else {
    Write-Error "Failed to push to GitHub."
}
