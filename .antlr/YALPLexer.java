// Generated from c:\Users\PARK JONGHYUN\Desktop\Universidad\Cuarto año\Segundo ciclo\compiladores\Lab0_UVG_COMPILADORES_2023\YALPCORREGIDO.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YALPLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, INT=20, ID=21, TYPE_ID=22, OBJECT_ID=23, STRING=24, 
		WS=25, CLASS=26, ELSE=27, FALSE=28, FI=29, IF=30, IN=31, INHERITS=32, 
		ISVOID=33, LOOP=34, POOL=35, THEN=36, WHILE=37, NEW=38, NOT=39, TRUE=40, 
		LET=41, CASE=42, OF=43, ESAC=44;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "INT", "ID", "TYPE_ID", "OBJECT_ID", "STRING", "WS", 
			"CLASS", "ELSE", "FALSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LOOP", 
			"POOL", "THEN", "WHILE", "NEW", "NOT", "TRUE", "LET", "CASE", "OF", "ESAC", 
			"LETTER", "DIGIT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "'}'", "':'", "';'", "'='", "'('", "')'", "','", "'<-'", 
			"'.'", "'@'", "'~'", "'*'", "'/'", "'+'", "'-'", "'<='", "'<'", "'=>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "INT", "ID", "TYPE_ID", 
			"OBJECT_ID", "STRING", "WS", "CLASS", "ELSE", "FALSE", "FI", "IF", "IN", 
			"INHERITS", "ISVOID", "LOOP", "POOL", "THEN", "WHILE", "NEW", "NOT", 
			"TRUE", "LET", "CASE", "OF", "ESAC"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public YALPLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "YALPCORREGIDO.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.\u011f\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7"+
		"\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17"+
		"\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25"+
		"\6\25\u008a\n\25\r\25\16\25\u008b\3\26\3\26\3\26\5\26\u0091\n\26\3\26"+
		"\3\26\3\26\7\26\u0096\n\26\f\26\16\26\u0099\13\26\3\27\3\27\3\27\3\27"+
		"\7\27\u009f\n\27\f\27\16\27\u00a2\13\27\3\30\3\30\3\30\3\30\7\30\u00a8"+
		"\n\30\f\30\16\30\u00ab\13\30\3\31\3\31\3\31\3\31\7\31\u00b1\n\31\f\31"+
		"\16\31\u00b4\13\31\3\31\3\31\3\32\6\32\u00b9\n\32\r\32\16\32\u00ba\3\32"+
		"\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35"+
		"\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3"+
		"!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3"+
		"$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3"+
		")\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3"+
		"/\3/\2\2\60\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33"+
		"\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67"+
		"\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2\3\2\30\3\2\62;\5\2\n"+
		"\f\16\16^^\6\2ddhhppvv\5\2\13\f\16\17\"\"\4\2EEee\4\2NNnn\4\2CCcc\4\2"+
		"UUuu\4\2GGgg\4\2HHhh\4\2KKkk\4\2PPpp\4\2JJjj\4\2TTtt\4\2VVvv\4\2XXxx\4"+
		"\2QQqq\4\2FFff\4\2RRrr\4\2YYyy\4\2WWww\4\2C\\c|\2\u012b\2\3\3\2\2\2\2"+
		"\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2"+
		"\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2"+
		"\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2"+
		"\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2"+
		"\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2"+
		"\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2"+
		"K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3"+
		"\2\2\2\2Y\3\2\2\2\3_\3\2\2\2\5a\3\2\2\2\7c\3\2\2\2\te\3\2\2\2\13g\3\2"+
		"\2\2\ri\3\2\2\2\17k\3\2\2\2\21m\3\2\2\2\23o\3\2\2\2\25r\3\2\2\2\27t\3"+
		"\2\2\2\31v\3\2\2\2\33x\3\2\2\2\35z\3\2\2\2\37|\3\2\2\2!~\3\2\2\2#\u0080"+
		"\3\2\2\2%\u0083\3\2\2\2\'\u0085\3\2\2\2)\u0089\3\2\2\2+\u0090\3\2\2\2"+
		"-\u009a\3\2\2\2/\u00a3\3\2\2\2\61\u00ac\3\2\2\2\63\u00b8\3\2\2\2\65\u00be"+
		"\3\2\2\2\67\u00c4\3\2\2\29\u00c9\3\2\2\2;\u00cf\3\2\2\2=\u00d2\3\2\2\2"+
		"?\u00d5\3\2\2\2A\u00d8\3\2\2\2C\u00e1\3\2\2\2E\u00e8\3\2\2\2G\u00ed\3"+
		"\2\2\2I\u00f2\3\2\2\2K\u00f7\3\2\2\2M\u00fd\3\2\2\2O\u0101\3\2\2\2Q\u0105"+
		"\3\2\2\2S\u010a\3\2\2\2U\u010e\3\2\2\2W\u0113\3\2\2\2Y\u0116\3\2\2\2["+
		"\u011b\3\2\2\2]\u011d\3\2\2\2_`\7}\2\2`\4\3\2\2\2ab\7\177\2\2b\6\3\2\2"+
		"\2cd\7<\2\2d\b\3\2\2\2ef\7=\2\2f\n\3\2\2\2gh\7?\2\2h\f\3\2\2\2ij\7*\2"+
		"\2j\16\3\2\2\2kl\7+\2\2l\20\3\2\2\2mn\7.\2\2n\22\3\2\2\2op\7>\2\2pq\7"+
		"/\2\2q\24\3\2\2\2rs\7\60\2\2s\26\3\2\2\2tu\7B\2\2u\30\3\2\2\2vw\7\u0080"+
		"\2\2w\32\3\2\2\2xy\7,\2\2y\34\3\2\2\2z{\7\61\2\2{\36\3\2\2\2|}\7-\2\2"+
		"} \3\2\2\2~\177\7/\2\2\177\"\3\2\2\2\u0080\u0081\7>\2\2\u0081\u0082\7"+
		"?\2\2\u0082$\3\2\2\2\u0083\u0084\7>\2\2\u0084&\3\2\2\2\u0085\u0086\7?"+
		"\2\2\u0086\u0087\7@\2\2\u0087(\3\2\2\2\u0088\u008a\t\2\2\2\u0089\u0088"+
		"\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c"+
		"*\3\2\2\2\u008d\u0091\5[.\2\u008e\u0091\5]/\2\u008f\u0091\7a\2\2\u0090"+
		"\u008d\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0091\u0097\3\2"+
		"\2\2\u0092\u0096\5[.\2\u0093\u0096\5]/\2\u0094\u0096\7a\2\2\u0095\u0092"+
		"\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097"+
		"\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098,\3\2\2\2\u0099\u0097\3\2\2\2"+
		"\u009a\u00a0\5[.\2\u009b\u009f\5[.\2\u009c\u009f\5]/\2\u009d\u009f\7a"+
		"\2\2\u009e\u009b\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f"+
		"\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1.\3\2\2\2"+
		"\u00a2\u00a0\3\2\2\2\u00a3\u00a9\5[.\2\u00a4\u00a8\5[.\2\u00a5\u00a8\5"+
		"]/\2\u00a6\u00a8\7a\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7"+
		"\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2"+
		"\2\2\u00aa\60\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00b2\7$\2\2\u00ad\u00b1"+
		"\n\3\2\2\u00ae\u00af\7^\2\2\u00af\u00b1\t\4\2\2\u00b0\u00ad\3\2\2\2\u00b0"+
		"\u00ae\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2"+
		"\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b6\7$\2\2\u00b6"+
		"\62\3\2\2\2\u00b7\u00b9\t\5\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00ba\3\2\2"+
		"\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd"+
		"\b\32\2\2\u00bd\64\3\2\2\2\u00be\u00bf\t\6\2\2\u00bf\u00c0\t\7\2\2\u00c0"+
		"\u00c1\t\b\2\2\u00c1\u00c2\t\t\2\2\u00c2\u00c3\t\t\2\2\u00c3\66\3\2\2"+
		"\2\u00c4\u00c5\t\n\2\2\u00c5\u00c6\t\7\2\2\u00c6\u00c7\t\t\2\2\u00c7\u00c8"+
		"\t\n\2\2\u00c88\3\2\2\2\u00c9\u00ca\t\13\2\2\u00ca\u00cb\t\b\2\2\u00cb"+
		"\u00cc\t\7\2\2\u00cc\u00cd\t\t\2\2\u00cd\u00ce\t\n\2\2\u00ce:\3\2\2\2"+
		"\u00cf\u00d0\t\13\2\2\u00d0\u00d1\t\f\2\2\u00d1<\3\2\2\2\u00d2\u00d3\t"+
		"\f\2\2\u00d3\u00d4\t\13\2\2\u00d4>\3\2\2\2\u00d5\u00d6\t\f\2\2\u00d6\u00d7"+
		"\t\r\2\2\u00d7@\3\2\2\2\u00d8\u00d9\t\f\2\2\u00d9\u00da\t\r\2\2\u00da"+
		"\u00db\t\16\2\2\u00db\u00dc\t\n\2\2\u00dc\u00dd\t\17\2\2\u00dd\u00de\t"+
		"\f\2\2\u00de\u00df\t\20\2\2\u00df\u00e0\t\t\2\2\u00e0B\3\2\2\2\u00e1\u00e2"+
		"\t\f\2\2\u00e2\u00e3\t\t\2\2\u00e3\u00e4\t\21\2\2\u00e4\u00e5\t\22\2\2"+
		"\u00e5\u00e6\t\f\2\2\u00e6\u00e7\t\23\2\2\u00e7D\3\2\2\2\u00e8\u00e9\t"+
		"\7\2\2\u00e9\u00ea\t\22\2\2\u00ea\u00eb\t\22\2\2\u00eb\u00ec\t\24\2\2"+
		"\u00ecF\3\2\2\2\u00ed\u00ee\t\24\2\2\u00ee\u00ef\t\22\2\2\u00ef\u00f0"+
		"\t\22\2\2\u00f0\u00f1\t\7\2\2\u00f1H\3\2\2\2\u00f2\u00f3\t\20\2\2\u00f3"+
		"\u00f4\t\16\2\2\u00f4\u00f5\t\n\2\2\u00f5\u00f6\t\r\2\2\u00f6J\3\2\2\2"+
		"\u00f7\u00f8\t\25\2\2\u00f8\u00f9\t\16\2\2\u00f9\u00fa\t\f\2\2\u00fa\u00fb"+
		"\t\7\2\2\u00fb\u00fc\t\n\2\2\u00fcL\3\2\2\2\u00fd\u00fe\t\r\2\2\u00fe"+
		"\u00ff\t\n\2\2\u00ff\u0100\t\25\2\2\u0100N\3\2\2\2\u0101\u0102\t\r\2\2"+
		"\u0102\u0103\t\22\2\2\u0103\u0104\t\20\2\2\u0104P\3\2\2\2\u0105\u0106"+
		"\t\20\2\2\u0106\u0107\t\17\2\2\u0107\u0108\t\26\2\2\u0108\u0109\t\n\2"+
		"\2\u0109R\3\2\2\2\u010a\u010b\t\7\2\2\u010b\u010c\t\n\2\2\u010c\u010d"+
		"\t\20\2\2\u010dT\3\2\2\2\u010e\u010f\t\6\2\2\u010f\u0110\t\b\2\2\u0110"+
		"\u0111\t\t\2\2\u0111\u0112\t\n\2\2\u0112V\3\2\2\2\u0113\u0114\t\22\2\2"+
		"\u0114\u0115\t\13\2\2\u0115X\3\2\2\2\u0116\u0117\t\n\2\2\u0117\u0118\t"+
		"\t\2\2\u0118\u0119\t\b\2\2\u0119\u011a\t\6\2\2\u011aZ\3\2\2\2\u011b\u011c"+
		"\t\27\2\2\u011c\\\3\2\2\2\u011d\u011e\t\2\2\2\u011e^\3\2\2\2\16\2\u008b"+
		"\u0090\u0095\u0097\u009e\u00a0\u00a7\u00a9\u00b0\u00b2\u00ba\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}