// Generated from c:/Users/PARK JONGHYUN/Desktop/Universidad/Cuarto año/Segundo ciclo/compiladores/Lab0_UVG_COMPILADORES_2023/YAPL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link YAPLParser}.
 */
public interface YAPLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by the {@code start}
	 * labeled alternative in {@link YAPLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterStart(YAPLParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by the {@code start}
	 * labeled alternative in {@link YAPLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitStart(YAPLParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by the {@code defClase}
	 * labeled alternative in {@link YAPLParser#classDefine}.
	 * @param ctx the parse tree
	 */
	void enterDefClase(YAPLParser.DefClaseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code defClase}
	 * labeled alternative in {@link YAPLParser#classDefine}.
	 * @param ctx the parse tree
	 */
	void exitDefClase(YAPLParser.DefClaseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code method}
	 * labeled alternative in {@link YAPLParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterMethod(YAPLParser.MethodContext ctx);
	/**
	 * Exit a parse tree produced by the {@code method}
	 * labeled alternative in {@link YAPLParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitMethod(YAPLParser.MethodContext ctx);
	/**
	 * Enter a parse tree produced by the {@code property}
	 * labeled alternative in {@link YAPLParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterProperty(YAPLParser.PropertyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code property}
	 * labeled alternative in {@link YAPLParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitProperty(YAPLParser.PropertyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code forml}
	 * labeled alternative in {@link YAPLParser#formal}.
	 * @param ctx the parse tree
	 */
	void enterForml(YAPLParser.FormlContext ctx);
	/**
	 * Exit a parse tree produced by the {@code forml}
	 * labeled alternative in {@link YAPLParser#formal}.
	 * @param ctx the parse tree
	 */
	void exitForml(YAPLParser.FormlContext ctx);
	/**
	 * Enter a parse tree produced by the {@code sub}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterSub(YAPLParser.SubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code sub}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitSub(YAPLParser.SubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code string}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterString(YAPLParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code string}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitString(YAPLParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mul}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMul(YAPLParser.MulContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mul}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMul(YAPLParser.MulContext ctx);
	/**
	 * Enter a parse tree produced by the {@code lteq}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLteq(YAPLParser.LteqContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lteq}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLteq(YAPLParser.LteqContext ctx);
	/**
	 * Enter a parse tree produced by the {@code lt}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLt(YAPLParser.LtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lt}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLt(YAPLParser.LtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code while}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterWhile(YAPLParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code while}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitWhile(YAPLParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code div}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDiv(YAPLParser.DivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code div}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDiv(YAPLParser.DivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code not}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNot(YAPLParser.NotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code not}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNot(YAPLParser.NotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code newObject}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNewObject(YAPLParser.NewObjectContext ctx);
	/**
	 * Exit a parse tree produced by the {@code newObject}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNewObject(YAPLParser.NewObjectContext ctx);
	/**
	 * Enter a parse tree produced by the {@code and}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAnd(YAPLParser.AndContext ctx);
	/**
	 * Exit a parse tree produced by the {@code and}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAnd(YAPLParser.AndContext ctx);
	/**
	 * Enter a parse tree produced by the {@code block}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBlock(YAPLParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by the {@code block}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBlock(YAPLParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by the {@code let}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLet(YAPLParser.LetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code let}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLet(YAPLParser.LetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code id}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterId(YAPLParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code id}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitId(YAPLParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code if}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIf(YAPLParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by the {@code if}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIf(YAPLParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ownMethodCall}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOwnMethodCall(YAPLParser.OwnMethodCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ownMethodCall}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOwnMethodCall(YAPLParser.OwnMethodCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code INTEGER}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterINTEGER(YAPLParser.INTEGERContext ctx);
	/**
	 * Exit a parse tree produced by the {@code INTEGER}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitINTEGER(YAPLParser.INTEGERContext ctx);
	/**
	 * Enter a parse tree produced by the {@code add}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAdd(YAPLParser.AddContext ctx);
	/**
	 * Exit a parse tree produced by the {@code add}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAdd(YAPLParser.AddContext ctx);
	/**
	 * Enter a parse tree produced by the {@code void}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVoid(YAPLParser.VoidContext ctx);
	/**
	 * Exit a parse tree produced by the {@code void}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVoid(YAPLParser.VoidContext ctx);
	/**
	 * Enter a parse tree produced by the {@code or}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOr(YAPLParser.OrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code or}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOr(YAPLParser.OrContext ctx);
	/**
	 * Enter a parse tree produced by the {@code invert}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterInvert(YAPLParser.InvertContext ctx);
	/**
	 * Exit a parse tree produced by the {@code invert}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitInvert(YAPLParser.InvertContext ctx);
	/**
	 * Enter a parse tree produced by the {@code factExpr}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFactExpr(YAPLParser.FactExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code factExpr}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFactExpr(YAPLParser.FactExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code false}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFalse(YAPLParser.FalseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code false}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFalse(YAPLParser.FalseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code equal}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterEqual(YAPLParser.EqualContext ctx);
	/**
	 * Exit a parse tree produced by the {@code equal}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitEqual(YAPLParser.EqualContext ctx);
	/**
	 * Enter a parse tree produced by the {@code true}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterTrue(YAPLParser.TrueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code true}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitTrue(YAPLParser.TrueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assign}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAssign(YAPLParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assign}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAssign(YAPLParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code methodCall}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMethodCall(YAPLParser.MethodCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code methodCall}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMethodCall(YAPLParser.MethodCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nestedLet}
	 * labeled alternative in {@link YAPLParser#let_expr}.
	 * @param ctx the parse tree
	 */
	void enterNestedLet(YAPLParser.NestedLetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nestedLet}
	 * labeled alternative in {@link YAPLParser#let_expr}.
	 * @param ctx the parse tree
	 */
	void exitNestedLet(YAPLParser.NestedLetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code letIn}
	 * labeled alternative in {@link YAPLParser#let_expr}.
	 * @param ctx the parse tree
	 */
	void enterLetIn(YAPLParser.LetInContext ctx);
	/**
	 * Exit a parse tree produced by the {@code letIn}
	 * labeled alternative in {@link YAPLParser#let_expr}.
	 * @param ctx the parse tree
	 */
	void exitLetIn(YAPLParser.LetInContext ctx);
	/**
	 * Enter a parse tree produced by the {@code letAssignLet}
	 * labeled alternative in {@link YAPLParser#let_expr}.
	 * @param ctx the parse tree
	 */
	void enterLetAssignLet(YAPLParser.LetAssignLetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code letAssignLet}
	 * labeled alternative in {@link YAPLParser#let_expr}.
	 * @param ctx the parse tree
	 */
	void exitLetAssignLet(YAPLParser.LetAssignLetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code letAssignIn}
	 * labeled alternative in {@link YAPLParser#let_expr}.
	 * @param ctx the parse tree
	 */
	void enterLetAssignIn(YAPLParser.LetAssignInContext ctx);
	/**
	 * Exit a parse tree produced by the {@code letAssignIn}
	 * labeled alternative in {@link YAPLParser#let_expr}.
	 * @param ctx the parse tree
	 */
	void exitLetAssignIn(YAPLParser.LetAssignInContext ctx);
}