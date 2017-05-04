# 2017.05.04 15:34:14 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/plat-mac/Carbon/Sound.py


def FOUR_CHAR_CODE(x):
    return x


soundListRsrc = FOUR_CHAR_CODE('snd ')
kSimpleBeepID = 1
rate32khz = 2097152000
rate22050hz = 1445068800
rate22khz = 1458473891
rate16khz = 1048576000
rate11khz = 729236945
rate11025hz = 722534400
rate8khz = 524288000
sampledSynth = 5
squareWaveSynth = 1
waveTableSynth = 3
MACE3snthID = 11
MACE6snthID = 13
kMiddleC = 60
kNoVolume = 0
kFullVolume = 256
stdQLength = 128
dataOffsetFlag = 32768
kUseOptionalOutputDevice = -1
notCompressed = 0
fixedCompression = -1
variableCompression = -2
twoToOne = 1
eightToThree = 2
threeToOne = 3
sixToOne = 4
sixToOnePacketSize = 8
threeToOnePacketSize = 16
stateBlockSize = 64
leftOverBlockSize = 32
firstSoundFormat = 1
secondSoundFormat = 2
dbBufferReady = 1
dbLastBuffer = 4
sysBeepDisable = 0
sysBeepEnable = 1
sysBeepSynchronous = 2
unitTypeNoSelection = 65535
unitTypeSeconds = 0
stdSH = 0
extSH = 255
cmpSH = 254
nullCmd = 0
quietCmd = 3
flushCmd = 4
reInitCmd = 5
waitCmd = 10
pauseCmd = 11
resumeCmd = 12
callBackCmd = 13
syncCmd = 14
availableCmd = 24
versionCmd = 25
volumeCmd = 46
getVolumeCmd = 47
clockComponentCmd = 50
getClockComponentCmd = 51
scheduledSoundCmd = 52
linkSoundComponentsCmd = 53
soundCmd = 80
bufferCmd = 81
rateMultiplierCmd = 86
getRateMultiplierCmd = 87
initCmd = 1
freeCmd = 2
totalLoadCmd = 26
loadCmd = 27
freqDurationCmd = 40
restCmd = 41
freqCmd = 42
ampCmd = 43
timbreCmd = 44
getAmpCmd = 45
waveTableCmd = 60
phaseCmd = 61
rateCmd = 82
continueCmd = 83
doubleBufferCmd = 84
getRateCmd = 85
sizeCmd = 90
convertCmd = 91
waveInitChannelMask = 7
waveInitChannel0 = 4
waveInitChannel1 = 5
waveInitChannel2 = 6
waveInitChannel3 = 7
initChan0 = waveInitChannel0
initChan1 = waveInitChannel1
initChan2 = waveInitChannel2
initChan3 = waveInitChannel3
outsideCmpSH = 0
insideCmpSH = 1
aceSuccess = 0
aceMemFull = 1
aceNilBlock = 2
aceBadComp = 3
aceBadEncode = 4
aceBadDest = 5
aceBadCmd = 6
initChanLeft = 2
initChanRight = 3
initNoInterp = 4
initNoDrop = 8
initMono = 128
initStereo = 192
initMACE3 = 768
initMACE6 = 1024
initPanMask = 3
initSRateMask = 48
initStereoMask = 192
initCompMask = 65280
siActiveChannels = FOUR_CHAR_CODE('chac')
siActiveLevels = FOUR_CHAR_CODE('lmac')
siAGCOnOff = FOUR_CHAR_CODE('agc ')
siAsync = FOUR_CHAR_CODE('asyn')
siAVDisplayBehavior = FOUR_CHAR_CODE('avdb')
siChannelAvailable = FOUR_CHAR_CODE('chav')
siCompressionAvailable = FOUR_CHAR_CODE('cmav')
siCompressionChannels = FOUR_CHAR_CODE('cpct')
siCompressionFactor = FOUR_CHAR_CODE('cmfa')
siCompressionHeader = FOUR_CHAR_CODE('cmhd')
siCompressionNames = FOUR_CHAR_CODE('cnam')
siCompressionParams = FOUR_CHAR_CODE('evaw')
siCompressionSampleRate = FOUR_CHAR_CODE('cprt')
siCompressionType = FOUR_CHAR_CODE('comp')
siContinuous = FOUR_CHAR_CODE('cont')
siDecompressionParams = FOUR_CHAR_CODE('wave')
siDeviceBufferInfo = FOUR_CHAR_CODE('dbin')
siDeviceConnected = FOUR_CHAR_CODE('dcon')
siDeviceIcon = FOUR_CHAR_CODE('icon')
siDeviceName = FOUR_CHAR_CODE('name')
siEQSpectrumBands = FOUR_CHAR_CODE('eqsb')
siEQSpectrumLevels = FOUR_CHAR_CODE('eqlv')
siEQSpectrumOnOff = FOUR_CHAR_CODE('eqlo')
siEQSpectrumResolution = FOUR_CHAR_CODE('eqrs')
siEQToneControlGain = FOUR_CHAR_CODE('eqtg')
siEQToneControlOnOff = FOUR_CHAR_CODE('eqtc')
siHardwareBalance = FOUR_CHAR_CODE('hbal')
siHardwareBalanceSteps = FOUR_CHAR_CODE('hbls')
siHardwareBass = FOUR_CHAR_CODE('hbas')
siHardwareBassSteps = FOUR_CHAR_CODE('hbst')
siHardwareBusy = FOUR_CHAR_CODE('hwbs')
siHardwareFormat = FOUR_CHAR_CODE('hwfm')
siHardwareMute = FOUR_CHAR_CODE('hmut')
siHardwareMuteNoPrefs = FOUR_CHAR_CODE('hmnp')
siHardwareTreble = FOUR_CHAR_CODE('htrb')
siHardwareTrebleSteps = FOUR_CHAR_CODE('hwts')
siHardwareVolume = FOUR_CHAR_CODE('hvol')
siHardwareVolumeSteps = FOUR_CHAR_CODE('hstp')
siHeadphoneMute = FOUR_CHAR_CODE('pmut')
siHeadphoneVolume = FOUR_CHAR_CODE('pvol')
siHeadphoneVolumeSteps = FOUR_CHAR_CODE('hdst')
siInputAvailable = FOUR_CHAR_CODE('inav')
siInputGain = FOUR_CHAR_CODE('gain')
siInputSource = FOUR_CHAR_CODE('sour')
siInputSourceNames = FOUR_CHAR_CODE('snam')
siLevelMeterOnOff = FOUR_CHAR_CODE('lmet')
siModemGain = FOUR_CHAR_CODE('mgai')
siMonitorAvailable = FOUR_CHAR_CODE('mnav')
siMonitorSource = FOUR_CHAR_CODE('mons')
siNumberChannels = FOUR_CHAR_CODE('chan')
siOptionsDialog = FOUR_CHAR_CODE('optd')
siOSTypeInputSource = FOUR_CHAR_CODE('inpt')
siOSTypeInputAvailable = FOUR_CHAR_CODE('inav')
siOutputDeviceName = FOUR_CHAR_CODE('onam')
siPlayThruOnOff = FOUR_CHAR_CODE('plth')
siPostMixerSoundComponent = FOUR_CHAR_CODE('psmx')
siPreMixerSoundComponent = FOUR_CHAR_CODE('prmx')
siQuality = FOUR_CHAR_CODE('qual')
siRateMultiplier = FOUR_CHAR_CODE('rmul')
siRecordingQuality = FOUR_CHAR_CODE('qual')
siSampleRate = FOUR_CHAR_CODE('srat')
siSampleRateAvailable = FOUR_CHAR_CODE('srav')
siSampleSize = FOUR_CHAR_CODE('ssiz')
siSampleSizeAvailable = FOUR_CHAR_CODE('ssav')
siSetupCDAudio = FOUR_CHAR_CODE('sucd')
siSetupModemAudio = FOUR_CHAR_CODE('sumd')
siSlopeAndIntercept = FOUR_CHAR_CODE('flap')
siSoundClock = FOUR_CHAR_CODE('sclk')
siUseThisSoundClock = FOUR_CHAR_CODE('sclc')
siSpeakerMute = FOUR_CHAR_CODE('smut')
siSpeakerVolume = FOUR_CHAR_CODE('svol')
siSSpCPULoadLimit = FOUR_CHAR_CODE('3dll')
siSSpLocalization = FOUR_CHAR_CODE('3dif')
siSSpSpeakerSetup = FOUR_CHAR_CODE('3dst')
siStereoInputGain = FOUR_CHAR_CODE('sgai')
siSubwooferMute = FOUR_CHAR_CODE('bmut')
siTerminalType = FOUR_CHAR_CODE('ttyp')
siTwosComplementOnOff = FOUR_CHAR_CODE('twos')
siVendorProduct = FOUR_CHAR_CODE('vpro')
siVolume = FOUR_CHAR_CODE('volu')
siVoxRecordInfo = FOUR_CHAR_CODE('voxr')
siVoxStopInfo = FOUR_CHAR_CODE('voxs')
siWideStereo = FOUR_CHAR_CODE('wide')
siSupportedExtendedFlags = FOUR_CHAR_CODE('exfl')
siRateConverterRollOffSlope = FOUR_CHAR_CODE('rcdb')
siOutputLatency = FOUR_CHAR_CODE('olte')
siCloseDriver = FOUR_CHAR_CODE('clos')
siInitializeDriver = FOUR_CHAR_CODE('init')
siPauseRecording = FOUR_CHAR_CODE('paus')
siUserInterruptProc = FOUR_CHAR_CODE('user')
kNoSource = FOUR_CHAR_CODE('none')
kCDSource = FOUR_CHAR_CODE('cd  ')
kExtMicSource = FOUR_CHAR_CODE('emic')
kSoundInSource = FOUR_CHAR_CODE('sinj')
kRCAInSource = FOUR_CHAR_CODE('irca')
kTVFMTunerSource = FOUR_CHAR_CODE('tvfm')
kDAVInSource = FOUR_CHAR_CODE('idav')
kIntMicSource = FOUR_CHAR_CODE('imic')
kMediaBaySource = FOUR_CHAR_CODE('mbay')
kModemSource = FOUR_CHAR_CODE('modm')
kPCCardSource = FOUR_CHAR_CODE('pcm ')
kZoomVideoSource = FOUR_CHAR_CODE('zvpc')
kDVDSource = FOUR_CHAR_CODE('dvda')
kMicrophoneArray = FOUR_CHAR_CODE('mica')
kNoSoundComponentType = FOUR_CHAR_CODE('****')
kSoundComponentType = FOUR_CHAR_CODE('sift')
kSoundComponentPPCType = FOUR_CHAR_CODE('nift')
kRate8SubType = FOUR_CHAR_CODE('ratb')
kRate16SubType = FOUR_CHAR_CODE('ratw')
kConverterSubType = FOUR_CHAR_CODE('conv')
kSndSourceSubType = FOUR_CHAR_CODE('sour')
kMixerType = FOUR_CHAR_CODE('mixr')
kMixer8SubType = FOUR_CHAR_CODE('mixb')
kMixer16SubType = FOUR_CHAR_CODE('mixw')
kSoundInputDeviceType = FOUR_CHAR_CODE('sinp')
kWaveInSubType = FOUR_CHAR_CODE('wavi')
kWaveInSnifferSubType = FOUR_CHAR_CODE('wisn')
kSoundOutputDeviceType = FOUR_CHAR_CODE('sdev')
kClassicSubType = FOUR_CHAR_CODE('clas')
kASCSubType = FOUR_CHAR_CODE('asc ')
kDSPSubType = FOUR_CHAR_CODE('dsp ')
kAwacsSubType = FOUR_CHAR_CODE('awac')
kGCAwacsSubType = FOUR_CHAR_CODE('awgc')
kSingerSubType = FOUR_CHAR_CODE('sing')
kSinger2SubType = FOUR_CHAR_CODE('sng2')
kWhitSubType = FOUR_CHAR_CODE('whit')
kSoundBlasterSubType = FOUR_CHAR_CODE('sbls')
kWaveOutSubType = FOUR_CHAR_CODE('wavo')
kWaveOutSnifferSubType = FOUR_CHAR_CODE('wosn')
kDirectSoundSubType = FOUR_CHAR_CODE('dsnd')
kDirectSoundSnifferSubType = FOUR_CHAR_CODE('dssn')
kUNIXsdevSubType = FOUR_CHAR_CODE('un1x')
kUSBSubType = FOUR_CHAR_CODE('usb ')
kBlueBoxSubType = FOUR_CHAR_CODE('bsnd')
kSoundCompressor = FOUR_CHAR_CODE('scom')
kSoundDecompressor = FOUR_CHAR_CODE('sdec')
kAudioComponentType = FOUR_CHAR_CODE('adio')
kAwacsPhoneSubType = FOUR_CHAR_CODE('hphn')
kAudioVisionSpeakerSubType = FOUR_CHAR_CODE('telc')
kAudioVisionHeadphoneSubType = FOUR_CHAR_CODE('telh')
kPhilipsFaderSubType = FOUR_CHAR_CODE('tvav')
kSGSToneSubType = FOUR_CHAR_CODE('sgs0')
kSoundEffectsType = FOUR_CHAR_CODE('snfx')
kEqualizerSubType = FOUR_CHAR_CODE('eqal')
kSSpLocalizationSubType = FOUR_CHAR_CODE('snd3')
kSoundNotCompressed = FOUR_CHAR_CODE('NONE')
k8BitOffsetBinaryFormat = FOUR_CHAR_CODE('raw ')
k16BitBigEndianFormat = FOUR_CHAR_CODE('twos')
k16BitLittleEndianFormat = FOUR_CHAR_CODE('sowt')
kFloat32Format = FOUR_CHAR_CODE('fl32')
kFloat64Format = FOUR_CHAR_CODE('fl64')
k24BitFormat = FOUR_CHAR_CODE('in24')
k32BitFormat = FOUR_CHAR_CODE('in32')
k32BitLittleEndianFormat = FOUR_CHAR_CODE('23ni')
kMACE3Compression = FOUR_CHAR_CODE('MAC3')
kMACE6Compression = FOUR_CHAR_CODE('MAC6')
kCDXA4Compression = FOUR_CHAR_CODE('cdx4')
kCDXA2Compression = FOUR_CHAR_CODE('cdx2')
kIMACompression = FOUR_CHAR_CODE('ima4')
kULawCompression = FOUR_CHAR_CODE('ulaw')
kALawCompression = FOUR_CHAR_CODE('alaw')
kMicrosoftADPCMFormat = 1836253186
kDVIIntelIMAFormat = 1836253201
kDVAudioFormat = FOUR_CHAR_CODE('dvca')
kQDesignCompression = FOUR_CHAR_CODE('QDMC')
kQDesign2Compression = FOUR_CHAR_CODE('QDM2')
kQUALCOMMCompression = FOUR_CHAR_CODE('Qclp')
kOffsetBinary = k8BitOffsetBinaryFormat
kTwosComplement = k16BitBigEndianFormat
kLittleEndianFormat = k16BitLittleEndianFormat
kMPEGLayer3Format = 1836253269
kFullMPEGLay3Format = FOUR_CHAR_CODE('.mp3')
k16BitNativeEndianFormat = k16BitLittleEndianFormat
k16BitNonNativeEndianFormat = k16BitBigEndianFormat
k16BitNativeEndianFormat = k16BitBigEndianFormat
k16BitNonNativeEndianFormat = k16BitLittleEndianFormat
k8BitRawIn = 1
k8BitTwosIn = 2
k16BitIn = 4
kStereoIn = 8
k8BitRawOut = 256
k8BitTwosOut = 512
k16BitOut = 1024
kStereoOut = 2048
kReverse = 65536L
kRateConvert = 131072L
kCreateSoundSource = 262144L
kVMAwareness = 2097152L
kHighQuality = 4194304L
kNonRealTime = 8388608L
kSourcePaused = 1
kPassThrough = 65536L
kNoSoundComponentChain = 131072L
kNoMixing = 1
kNoSampleRateConversion = 2
kNoSampleSizeConversion = 4
kNoSampleFormatConversion = 8
kNoChannelConversion = 16
kNoDecompression = 32
kNoVolumeConversion = 64
kNoRealtimeProcessing = 128
kScheduledSource = 256
kNonInterleavedBuffer = 512
kNonPagingMixer = 1024
kSoundConverterMixer = 2048
kPagingMixer = 4096
kVMAwareMixer = 8192
kExtendedSoundData = 16384
kBestQuality = 1
kInputMask = 255
kOutputMask = 65280
kOutputShift = 8
kActionMask = 16711680
kSoundComponentBits = 16777215
kAudioFormatAtomType = FOUR_CHAR_CODE('frma')
kAudioEndianAtomType = FOUR_CHAR_CODE('enda')
kAudioVBRAtomType = FOUR_CHAR_CODE('vbra')
kAudioTerminatorAtomType = 0
kAVDisplayHeadphoneRemove = 0
kAVDisplayHeadphoneInsert = 1
kAVDisplayPlainTalkRemove = 2
kAVDisplayPlainTalkInsert = 3
audioAllChannels = 0
audioLeftChannel = 1
audioRightChannel = 2
audioUnmuted = 0
audioMuted = 1
audioDoesMono = 1L
audioDoesStereo = 2L
audioDoesIndependentChannels = 4L
siCDQuality = FOUR_CHAR_CODE('cd  ')
siBestQuality = FOUR_CHAR_CODE('best')
siBetterQuality = FOUR_CHAR_CODE('betr')
siGoodQuality = FOUR_CHAR_CODE('good')
siNoneQuality = FOUR_CHAR_CODE('none')
siDeviceIsConnected = 1
siDeviceNotConnected = 0
siDontKnowIfConnected = -1
siReadPermission = 0
siWritePermission = 1
kSoundConverterDidntFillBuffer = 1
kSoundConverterHasLeftOverData = 2
kExtendedSoundSampleCountNotValid = 1L
kExtendedSoundBufferSizeValid = 2L
kScheduledSoundDoScheduled = 1
kScheduledSoundDoCallBack = 2
kScheduledSoundExtendedHdr = 4
kSoundComponentInitOutputDeviceSelect = 1
kSoundComponentSetSourceSelect = 2
kSoundComponentGetSourceSelect = 3
kSoundComponentGetSourceDataSelect = 4
kSoundComponentSetOutputSelect = 5
kSoundComponentAddSourceSelect = 257
kSoundComponentRemoveSourceSelect = 258
kSoundComponentGetInfoSelect = 259
kSoundComponentSetInfoSelect = 260
kSoundComponentStartSourceSelect = 261
kSoundComponentStopSourceSelect = 262
kSoundComponentPauseSourceSelect = 263
kSoundComponentPlaySourceBufferSelect = 264
kAudioGetVolumeSelect = 0
kAudioSetVolumeSelect = 1
kAudioGetMuteSelect = 2
kAudioSetMuteSelect = 3
kAudioSetToDefaultsSelect = 4
kAudioGetInfoSelect = 5
kAudioGetBassSelect = 6
kAudioSetBassSelect = 7
kAudioGetTrebleSelect = 8
kAudioSetTrebleSelect = 9
kAudioGetOutputDeviceSelect = 10
kAudioMuteOnEventSelect = 129
kDelegatedSoundComponentSelectors = 256
kSndInputReadAsyncSelect = 1
kSndInputReadSyncSelect = 2
kSndInputPauseRecordingSelect = 3
kSndInputResumeRecordingSelect = 4
kSndInputStopRecordingSelect = 5
kSndInputGetStatusSelect = 6
kSndInputGetDeviceInfoSelect = 7
kSndInputSetDeviceInfoSelect = 8
kSndInputInitHardwareSelect = 9
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\plat-mac\Carbon\Sound.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:34:15 St�edn� Evropa (letn� �as)
