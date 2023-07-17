// Generated from c:\Users\PARK JONGHYUN\Desktop\Universidad\Cuarto año\Segundo ciclo\compiladores\Lab0_UVG_COMPILADORES_2023\YAPL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, ELSE=2, FI=3, IF=4, IN=5, INHERITS=6, ISVOID=7, LOOP=8, POOL=9, 
		THEN=10, WHILE=11, NEW=12, NOT=13, FALSE=14, TRUE=15, LET=16, NUM=17, 
		ID=18, TYPE=19, STRING=20, SEMICOLON=21, OPENBRACE=22, CLOSEBRACE=23, 
		COLON=24, COMMA=25, OPENPARENTHESES=26, CLOSEPARENTHESES=27, DOT=28, AT=29, 
		TILDE=30, ADD=31, SUB=32, MUL=33, DIV=34, EQUAL=35, LT=36, LTEQ=37, ASSIGN=38, 
		SINGLECOMMENT=39, MULTICOMMENT=40, WS=41, ERROR=42;
	public static final int
		RULE_program = 0, RULE_classDefine = 1, RULE_feature = 2, RULE_formal = 3, 
		RULE_expr = 4, RULE_let_expr = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classDefine", "feature", "formal", "expr", "let_expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, "'false'", "'true'", null, null, null, null, null, "';'", 
			"'{'", "'}'", "':'", "','", "'('", "')'", "'.'", "'@'", "'~'", "'+'", 
			"'-'", "'*'", "'/'", "'='", "'<'", "'<='", "'<-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", "ISVOID", "LOOP", 
			"POOL", "THEN", "WHILE", "NEW", "NOT", "FALSE", "TRUE", "LET", "NUM", 
			"ID", "TYPE", "STRING", "SEMICOLON", "OPENBRACE", "CLOSEBRACE", "COLON", 
			"COMMA", "OPENPARENTHESES", "CLOSEPARENTHESES", "DOT", "AT", "TILDE", 
			"ADD", "SUB", "MUL", "DIV", "EQUAL", "LT", "LTEQ", "ASSIGN", "SINGLECOMMENT", 
			"MULTICOMMENT", "WS", "ERROR"
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

	@Override
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YAPLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	 
		public ProgramContext() { }
		public void copyFrom(ProgramContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class StartContext extends ProgramContext {
		public List<ClassDefineContext> classDefine() {
			return getRuleContexts(ClassDefineContext.class);
		}
		public ClassDefineContext classDefine(int i) {
			return getRuleContext(ClassDefineContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YAPLParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YAPLParser.SEMICOLON, i);
		}
		public StartContext(ProgramContext ctx) { copyFrom(ctx); }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			_localctx = new StartContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(15); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(12);
				classDefine();
				setState(13);
				match(SEMICOLON);
				}
				}
				setState(17); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassDefineContext extends ParserRuleContext {
		public ClassDefineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDefine; }
	 
		public ClassDefineContext() { }
		public void copyFrom(ClassDefineContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class DefClaseContext extends ClassDefineContext {
		public TerminalNode CLASS() { return getToken(YAPLParser.CLASS, 0); }
		public List<TerminalNode> TYPE() { return getTokens(YAPLParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(YAPLParser.TYPE, i);
		}
		public TerminalNode OPENBRACE() { return getToken(YAPLParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(YAPLParser.CLOSEBRACE, 0); }
		public TerminalNode INHERITS() { return getToken(YAPLParser.INHERITS, 0); }
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YAPLParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YAPLParser.SEMICOLON, i);
		}
		public DefClaseContext(ClassDefineContext ctx) { copyFrom(ctx); }
	}

	public final ClassDefineContext classDefine() throws RecognitionException {
		ClassDefineContext _localctx = new ClassDefineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_classDefine);
		int _la;
		try {
			_localctx = new DefClaseContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			match(CLASS);
			setState(20);
			match(TYPE);
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(21);
				match(INHERITS);
				setState(22);
				match(TYPE);
				}
			}

			setState(25);
			match(OPENBRACE);
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(26);
				feature();
				setState(27);
				match(SEMICOLON);
				}
				}
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(34);
			match(CLOSEBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FeatureContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode OPENBRACE() { return getToken(YAPLParser.OPENBRACE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSEBRACE() { return getToken(YAPLParser.CLOSEBRACE, 0); }
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YAPLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLParser.COMMA, i);
		}
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_feature);
		int _la;
		try {
			setState(62);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				match(ID);
				setState(37);
				match(OPENPARENTHESES);
				setState(46);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(38);
					formal();
					setState(43);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(39);
						match(COMMA);
						setState(40);
						formal();
						}
						}
						setState(45);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(48);
				match(CLOSEPARENTHESES);
				setState(49);
				match(COLON);
				setState(50);
				match(TYPE);
				setState(51);
				match(OPENBRACE);
				setState(52);
				expr(0);
				setState(53);
				match(CLOSEBRACE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				match(ID);
				setState(56);
				match(COLON);
				setState(57);
				match(TYPE);
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(58);
					match(ASSIGN);
					setState(59);
					expr(0);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalContext extends ParserRuleContext {
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
	 
		public FormalContext() { }
		public void copyFrom(FormalContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class FormlContext extends FormalContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public FormlContext(FormalContext ctx) { copyFrom(ctx); }
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_formal);
		try {
			_localctx = new FormlContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(ID);
			setState(65);
			match(COLON);
			setState(66);
			match(TYPE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AddContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(YAPLParser.ADD, 0); }
		public AddContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class SubContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode SUB() { return getToken(YAPLParser.SUB, 0); }
		public SubContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class VoidContext extends ExprContext {
		public TerminalNode ISVOID() { return getToken(YAPLParser.ISVOID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public VoidContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class InvertContext extends ExprContext {
		public TerminalNode TILDE() { return getToken(YAPLParser.TILDE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public InvertContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class StringContext extends ExprContext {
		public TerminalNode STRING() { return getToken(YAPLParser.STRING, 0); }
		public StringContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MulContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(YAPLParser.MUL, 0); }
		public MulContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class FactExprContext extends ExprContext {
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public FactExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class LteqContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LTEQ() { return getToken(YAPLParser.LTEQ, 0); }
		public LteqContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NumContext extends ExprContext {
		public TerminalNode NUM() { return getToken(YAPLParser.NUM, 0); }
		public NumContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class FalseContext extends ExprContext {
		public TerminalNode FALSE() { return getToken(YAPLParser.FALSE, 0); }
		public FalseContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class LtContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LT() { return getToken(YAPLParser.LT, 0); }
		public LtContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class WhileContext extends ExprContext {
		public TerminalNode WHILE() { return getToken(YAPLParser.WHILE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LOOP() { return getToken(YAPLParser.LOOP, 0); }
		public TerminalNode POOL() { return getToken(YAPLParser.POOL, 0); }
		public WhileContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class DivContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DIV() { return getToken(YAPLParser.DIV, 0); }
		public DivContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class EqualContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode EQUAL() { return getToken(YAPLParser.EQUAL, 0); }
		public EqualContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NotContext extends ExprContext {
		public TerminalNode NOT() { return getToken(YAPLParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NotContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class NewObjectContext extends ExprContext {
		public TerminalNode NEW() { return getToken(YAPLParser.NEW, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public NewObjectContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class TrueContext extends ExprContext {
		public TerminalNode TRUE() { return getToken(YAPLParser.TRUE, 0); }
		public TrueContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class BlockContext extends ExprContext {
		public TerminalNode OPENBRACE() { return getToken(YAPLParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(YAPLParser.CLOSEBRACE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(YAPLParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(YAPLParser.SEMICOLON, i);
		}
		public BlockContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class LetContext extends ExprContext {
		public TerminalNode LET() { return getToken(YAPLParser.LET, 0); }
		public Let_exprContext let_expr() {
			return getRuleContext(Let_exprContext.class,0);
		}
		public LetContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IdContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public IdContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IfContext extends ExprContext {
		public TerminalNode IF() { return getToken(YAPLParser.IF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode THEN() { return getToken(YAPLParser.THEN, 0); }
		public TerminalNode ELSE() { return getToken(YAPLParser.ELSE, 0); }
		public TerminalNode FI() { return getToken(YAPLParser.FI, 0); }
		public IfContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class AssignContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class OwnMethodCallContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YAPLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLParser.COMMA, i);
		}
		public OwnMethodCallContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MethodCallContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DOT() { return getToken(YAPLParser.DOT, 0); }
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode OPENPARENTHESES() { return getToken(YAPLParser.OPENPARENTHESES, 0); }
		public TerminalNode CLOSEPARENTHESES() { return getToken(YAPLParser.CLOSEPARENTHESES, 0); }
		public TerminalNode AT() { return getToken(YAPLParser.AT, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(YAPLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLParser.COMMA, i);
		}
		public MethodCallContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				_localctx = new AssignContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(69);
				match(ID);
				setState(70);
				match(ASSIGN);
				setState(71);
				expr(24);
				}
				break;
			case 2:
				{
				_localctx = new OwnMethodCallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(72);
				match(ID);
				setState(73);
				match(OPENPARENTHESES);
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << FALSE) | (1L << TRUE) | (1L << LET) | (1L << NUM) | (1L << ID) | (1L << STRING) | (1L << OPENBRACE) | (1L << OPENPARENTHESES) | (1L << TILDE))) != 0)) {
					{
					setState(74);
					expr(0);
					setState(79);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(75);
						match(COMMA);
						setState(76);
						expr(0);
						}
						}
						setState(81);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(84);
				match(CLOSEPARENTHESES);
				}
				break;
			case 3:
				{
				_localctx = new IfContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(85);
				match(IF);
				setState(86);
				expr(0);
				setState(87);
				match(THEN);
				setState(88);
				expr(0);
				setState(89);
				match(ELSE);
				setState(90);
				expr(0);
				setState(91);
				match(FI);
				}
				break;
			case 4:
				{
				_localctx = new WhileContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(93);
				match(WHILE);
				setState(94);
				expr(0);
				setState(95);
				match(LOOP);
				setState(96);
				expr(0);
				setState(97);
				match(POOL);
				}
				break;
			case 5:
				{
				_localctx = new BlockContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(99);
				match(OPENBRACE);
				setState(103); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(100);
					expr(0);
					setState(101);
					match(SEMICOLON);
					}
					}
					setState(105); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << FALSE) | (1L << TRUE) | (1L << LET) | (1L << NUM) | (1L << ID) | (1L << STRING) | (1L << OPENBRACE) | (1L << OPENPARENTHESES) | (1L << TILDE))) != 0) );
				setState(107);
				match(CLOSEBRACE);
				}
				break;
			case 6:
				{
				_localctx = new LetContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(109);
				match(LET);
				setState(110);
				let_expr();
				}
				break;
			case 7:
				{
				_localctx = new NewObjectContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(111);
				match(NEW);
				setState(112);
				match(TYPE);
				}
				break;
			case 8:
				{
				_localctx = new VoidContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(113);
				match(ISVOID);
				setState(114);
				expr(16);
				}
				break;
			case 9:
				{
				_localctx = new InvertContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(115);
				match(TILDE);
				setState(116);
				expr(11);
				}
				break;
			case 10:
				{
				_localctx = new NotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(117);
				match(NOT);
				setState(118);
				expr(7);
				}
				break;
			case 11:
				{
				_localctx = new FactExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(119);
				match(OPENPARENTHESES);
				setState(120);
				expr(0);
				setState(121);
				match(CLOSEPARENTHESES);
				}
				break;
			case 12:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(123);
				match(ID);
				}
				break;
			case 13:
				{
				_localctx = new NumContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(124);
				match(NUM);
				}
				break;
			case 14:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(125);
				match(STRING);
				}
				break;
			case 15:
				{
				_localctx = new TrueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(126);
				match(TRUE);
				}
				break;
			case 16:
				{
				_localctx = new FalseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(127);
				match(FALSE);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(172);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(170);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new AddContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(130);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(131);
						match(ADD);
						setState(132);
						expr(16);
						}
						break;
					case 2:
						{
						_localctx = new SubContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(133);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(134);
						match(SUB);
						setState(135);
						expr(15);
						}
						break;
					case 3:
						{
						_localctx = new MulContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(136);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(137);
						match(MUL);
						setState(138);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new DivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(139);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(140);
						match(DIV);
						setState(141);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new LtContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(142);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(143);
						match(LT);
						setState(144);
						expr(11);
						}
						break;
					case 6:
						{
						_localctx = new LteqContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(145);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(146);
						match(LTEQ);
						setState(147);
						expr(10);
						}
						break;
					case 7:
						{
						_localctx = new EqualContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(148);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(149);
						match(EQUAL);
						setState(150);
						expr(9);
						}
						break;
					case 8:
						{
						_localctx = new MethodCallContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(151);
						if (!(precpred(_ctx, 23))) throw new FailedPredicateException(this, "precpred(_ctx, 23)");
						setState(154);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==AT) {
							{
							setState(152);
							match(AT);
							setState(153);
							match(TYPE);
							}
						}

						setState(156);
						match(DOT);
						setState(157);
						match(ID);
						setState(158);
						match(OPENPARENTHESES);
						setState(167);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << ISVOID) | (1L << WHILE) | (1L << NEW) | (1L << NOT) | (1L << FALSE) | (1L << TRUE) | (1L << LET) | (1L << NUM) | (1L << ID) | (1L << STRING) | (1L << OPENBRACE) | (1L << OPENPARENTHESES) | (1L << TILDE))) != 0)) {
							{
							setState(159);
							expr(0);
							setState(164);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==COMMA) {
								{
								{
								setState(160);
								match(COMMA);
								setState(161);
								expr(0);
								}
								}
								setState(166);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(169);
						match(CLOSEPARENTHESES);
						}
						break;
					}
					} 
				}
				setState(174);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Let_exprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode COMMA() { return getToken(YAPLParser.COMMA, 0); }
		public Let_exprContext let_expr() {
			return getRuleContext(Let_exprContext.class,0);
		}
		public TerminalNode IN() { return getToken(YAPLParser.IN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public Let_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_let_expr; }
	}

	public final Let_exprContext let_expr() throws RecognitionException {
		Let_exprContext _localctx = new Let_exprContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_let_expr);
		try {
			setState(201);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(175);
				match(ID);
				setState(176);
				match(COLON);
				setState(177);
				match(TYPE);
				setState(178);
				match(COMMA);
				setState(179);
				let_expr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(180);
				match(ID);
				setState(181);
				match(COLON);
				setState(182);
				match(TYPE);
				setState(183);
				match(IN);
				setState(184);
				expr(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(185);
				match(ID);
				setState(186);
				match(COLON);
				setState(187);
				match(TYPE);
				setState(188);
				match(ASSIGN);
				setState(189);
				expr(0);
				setState(190);
				match(COMMA);
				setState(191);
				let_expr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(193);
				match(ID);
				setState(194);
				match(COLON);
				setState(195);
				match(TYPE);
				setState(196);
				match(ASSIGN);
				setState(197);
				expr(0);
				setState(198);
				match(IN);
				setState(199);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 15);
		case 1:
			return precpred(_ctx, 14);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 10);
		case 5:
			return precpred(_ctx, 9);
		case 6:
			return precpred(_ctx, 8);
		case 7:
			return precpred(_ctx, 23);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u00ce\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\3\2\3\2\6\2\22\n\2\r\2\16\2"+
		"\23\3\3\3\3\3\3\3\3\5\3\32\n\3\3\3\3\3\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3"+
		"\3\3\3\3\3\4\3\4\3\4\3\4\3\4\7\4,\n\4\f\4\16\4/\13\4\5\4\61\n\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4?\n\4\5\4A\n\4\3\5\3\5\3"+
		"\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6P\n\6\f\6\16\6S\13\6\5\6"+
		"U\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\6\6j\n\6\r\6\16\6k\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0083\n\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\5\6\u009d\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00a5\n\6\f"+
		"\6\16\6\u00a8\13\6\5\6\u00aa\n\6\3\6\7\6\u00ad\n\6\f\6\16\6\u00b0\13\6"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00cc\n\7\3\7\2\3\n\b\2\4\6\b\n"+
		"\f\2\2\2\u00ee\2\21\3\2\2\2\4\25\3\2\2\2\6@\3\2\2\2\bB\3\2\2\2\n\u0082"+
		"\3\2\2\2\f\u00cb\3\2\2\2\16\17\5\4\3\2\17\20\7\27\2\2\20\22\3\2\2\2\21"+
		"\16\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25"+
		"\26\7\3\2\2\26\31\7\25\2\2\27\30\7\b\2\2\30\32\7\25\2\2\31\27\3\2\2\2"+
		"\31\32\3\2\2\2\32\33\3\2\2\2\33!\7\30\2\2\34\35\5\6\4\2\35\36\7\27\2\2"+
		"\36 \3\2\2\2\37\34\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2"+
		"#!\3\2\2\2$%\7\31\2\2%\5\3\2\2\2&\'\7\24\2\2\'\60\7\34\2\2(-\5\b\5\2)"+
		"*\7\33\2\2*,\5\b\5\2+)\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\61\3\2\2"+
		"\2/-\3\2\2\2\60(\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\63\7\35\2\2\63"+
		"\64\7\32\2\2\64\65\7\25\2\2\65\66\7\30\2\2\66\67\5\n\6\2\678\7\31\2\2"+
		"8A\3\2\2\29:\7\24\2\2:;\7\32\2\2;>\7\25\2\2<=\7(\2\2=?\5\n\6\2><\3\2\2"+
		"\2>?\3\2\2\2?A\3\2\2\2@&\3\2\2\2@9\3\2\2\2A\7\3\2\2\2BC\7\24\2\2CD\7\32"+
		"\2\2DE\7\25\2\2E\t\3\2\2\2FG\b\6\1\2GH\7\24\2\2HI\7(\2\2I\u0083\5\n\6"+
		"\32JK\7\24\2\2KT\7\34\2\2LQ\5\n\6\2MN\7\33\2\2NP\5\n\6\2OM\3\2\2\2PS\3"+
		"\2\2\2QO\3\2\2\2QR\3\2\2\2RU\3\2\2\2SQ\3\2\2\2TL\3\2\2\2TU\3\2\2\2UV\3"+
		"\2\2\2V\u0083\7\35\2\2WX\7\6\2\2XY\5\n\6\2YZ\7\f\2\2Z[\5\n\6\2[\\\7\4"+
		"\2\2\\]\5\n\6\2]^\7\5\2\2^\u0083\3\2\2\2_`\7\r\2\2`a\5\n\6\2ab\7\n\2\2"+
		"bc\5\n\6\2cd\7\13\2\2d\u0083\3\2\2\2ei\7\30\2\2fg\5\n\6\2gh\7\27\2\2h"+
		"j\3\2\2\2if\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2lm\3\2\2\2mn\7\31\2\2"+
		"n\u0083\3\2\2\2op\7\22\2\2p\u0083\5\f\7\2qr\7\16\2\2r\u0083\7\25\2\2s"+
		"t\7\t\2\2t\u0083\5\n\6\22uv\7 \2\2v\u0083\5\n\6\rwx\7\17\2\2x\u0083\5"+
		"\n\6\tyz\7\34\2\2z{\5\n\6\2{|\7\35\2\2|\u0083\3\2\2\2}\u0083\7\24\2\2"+
		"~\u0083\7\23\2\2\177\u0083\7\26\2\2\u0080\u0083\7\21\2\2\u0081\u0083\7"+
		"\20\2\2\u0082F\3\2\2\2\u0082J\3\2\2\2\u0082W\3\2\2\2\u0082_\3\2\2\2\u0082"+
		"e\3\2\2\2\u0082o\3\2\2\2\u0082q\3\2\2\2\u0082s\3\2\2\2\u0082u\3\2\2\2"+
		"\u0082w\3\2\2\2\u0082y\3\2\2\2\u0082}\3\2\2\2\u0082~\3\2\2\2\u0082\177"+
		"\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083\u00ae\3\2\2\2\u0084"+
		"\u0085\f\21\2\2\u0085\u0086\7!\2\2\u0086\u00ad\5\n\6\22\u0087\u0088\f"+
		"\20\2\2\u0088\u0089\7\"\2\2\u0089\u00ad\5\n\6\21\u008a\u008b\f\17\2\2"+
		"\u008b\u008c\7#\2\2\u008c\u00ad\5\n\6\20\u008d\u008e\f\16\2\2\u008e\u008f"+
		"\7$\2\2\u008f\u00ad\5\n\6\17\u0090\u0091\f\f\2\2\u0091\u0092\7&\2\2\u0092"+
		"\u00ad\5\n\6\r\u0093\u0094\f\13\2\2\u0094\u0095\7\'\2\2\u0095\u00ad\5"+
		"\n\6\f\u0096\u0097\f\n\2\2\u0097\u0098\7%\2\2\u0098\u00ad\5\n\6\13\u0099"+
		"\u009c\f\31\2\2\u009a\u009b\7\37\2\2\u009b\u009d\7\25\2\2\u009c\u009a"+
		"\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\7\36\2\2"+
		"\u009f\u00a0\7\24\2\2\u00a0\u00a9\7\34\2\2\u00a1\u00a6\5\n\6\2\u00a2\u00a3"+
		"\7\33\2\2\u00a3\u00a5\5\n\6\2\u00a4\u00a2\3\2\2\2\u00a5\u00a8\3\2\2\2"+
		"\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6"+
		"\3\2\2\2\u00a9\u00a1\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab"+
		"\u00ad\7\35\2\2\u00ac\u0084\3\2\2\2\u00ac\u0087\3\2\2\2\u00ac\u008a\3"+
		"\2\2\2\u00ac\u008d\3\2\2\2\u00ac\u0090\3\2\2\2\u00ac\u0093\3\2\2\2\u00ac"+
		"\u0096\3\2\2\2\u00ac\u0099\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2"+
		"\2\2\u00ae\u00af\3\2\2\2\u00af\13\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2"+
		"\7\24\2\2\u00b2\u00b3\7\32\2\2\u00b3\u00b4\7\25\2\2\u00b4\u00b5\7\33\2"+
		"\2\u00b5\u00cc\5\f\7\2\u00b6\u00b7\7\24\2\2\u00b7\u00b8\7\32\2\2\u00b8"+
		"\u00b9\7\25\2\2\u00b9\u00ba\7\7\2\2\u00ba\u00cc\5\n\6\2\u00bb\u00bc\7"+
		"\24\2\2\u00bc\u00bd\7\32\2\2\u00bd\u00be\7\25\2\2\u00be\u00bf\7(\2\2\u00bf"+
		"\u00c0\5\n\6\2\u00c0\u00c1\7\33\2\2\u00c1\u00c2\5\f\7\2\u00c2\u00cc\3"+
		"\2\2\2\u00c3\u00c4\7\24\2\2\u00c4\u00c5\7\32\2\2\u00c5\u00c6\7\25\2\2"+
		"\u00c6\u00c7\7(\2\2\u00c7\u00c8\5\n\6\2\u00c8\u00c9\7\7\2\2\u00c9\u00ca"+
		"\5\n\6\2\u00ca\u00cc\3\2\2\2\u00cb\u00b1\3\2\2\2\u00cb\u00b6\3\2\2\2\u00cb"+
		"\u00bb\3\2\2\2\u00cb\u00c3\3\2\2\2\u00cc\r\3\2\2\2\23\23\31!-\60>@QTk"+
		"\u0082\u009c\u00a6\u00a9\u00ac\u00ae\u00cb";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}